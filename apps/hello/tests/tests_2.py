import json
from apps.hello.models import UserProfile
from django.core.urlresolvers import reverse
from apps.hello.models import MyHttpRequest
from django.test import TestCase
from django.test.client import RequestFactory, Client
import re


class TestRequestView(TestCase):
    """ Test class for t3middleware app include tests: save request to db,
     show it on page, update page asynchronously
    """
    def test_save_request_to_db(self):
        """ each request should be saved in db """
        factory = RequestFactory()

        request = factory.get(reverse('index'))

        client = Client()
        client.get(reverse('index'))

        _request = MyHttpRequest.objects.first()
        kwargs = {
            'host': request.get_host(),
            'path': request.path,
            'method': request.method,
            'uri': request.build_absolute_uri(),
            'query_string': request.META['QUERY_STRING']
        }

        for key in kwargs.keys():
            self.assertEquals(kwargs[key], getattr(_request, key))

    def test_request_page_uses_right__template(self):
        """ /request/ page should use request.html """
        response = self.client.get(reverse('request'))

        self.assertTemplateUsed(response, 'hello/request.html')

    def test_custom_middleware_doesnt_save_ajax_requests(self):
        """ i've decided ignore  request from /request/ page"""
        self.client.get(reverse('index'))

        _count = MyHttpRequest.objects.count()

        self.client.post(reverse('getrequests'),
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(_count, MyHttpRequest.objects.count())
        self.assertNotEquals(_count, 0)

    def test_get_requests_retuns_not_viewed_request_number(self):
        """ requests number should updates asynchronously """
        self.client.get(reverse('index'))
        response = self.client.get(reverse('getrequests'),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data = json.loads(response.content)
        self.assertEquals(data['count'], MyHttpRequest.objects.filter(
            is_viewed=False).count())

        self.client.get(reverse('index'))
        response = self.client.get(reverse('getrequests'),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data = json.loads(response.content)
        self.assertEquals(data['count'], MyHttpRequest.objects.filter(
            is_viewed=False).count())

    def test_requests_count_updates_on_page_reload(self):
        """when /request/ page updates - all myhhtprequest objects sets ridden
        """
        self.client.get(reverse('index'))
        self.assertEquals(
            MyHttpRequest.objects.filter(is_viewed=False).count(), 1)

        self.client.get(reverse('request'))
        self.assertEquals(
            MyHttpRequest.objects.filter(is_viewed=False).count(), 0)

    def test_reqeust_page_shows_exactly_10_last_requests(self):
        """get_requests fn return 10 last requests"""
        self.client.get(reverse('request'))
        for i in range(9):
            self.client.get(reverse('index'))

        response = self.client.get(reverse('getrequests'))
        requests_string = json.loads(response.content)['text']
        requests = MyHttpRequest.objects.all().order_by('-time')[:10]
        for request in requests:
            self.assertIn(request.uri, requests_string)


class TestPriority(TestCase):
    """ testing  order by priority field"""
    def test_priority_sorts(self):
        """ test entities with higher priority goes earlier """
        for i in range(5):
            self.client.get(reverse('index'))
            _request = MyHttpRequest.objects.last()
            _request.priority = 4 - i
            _request.save()

        response = self.client.get(reverse('getrequests'),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        text = json.loads(response.content)['text']

        p = re.compile(ur'>(\d+)</div>')
        match = re.findall(p, text)

        res = ['%d' % (4 - i) for i in range(5)]

        self.assertEquals(match, res)


class TestNoData(TestCase):
    def test_error_msg_if_no_data(self):
        """error message on home page if no user_data in db"""
        UserProfile.objects.first().delete()
        response = self.client.get(reverse('index'))

        self.assertIn("Error: No data", response.content)
