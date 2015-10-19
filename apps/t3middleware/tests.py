import json
from django.core.urlresolvers import reverse
from .models import MyHttpRequest
from django.test import TestCase
from django.test.client import RequestFactory, Client


class TestRequestView(TestCase):
    """ Test class for t3middleware app include tests: save request to db,
     show it on page, update page asynchronously
    """
    fixtures = ['my_fixture.json']

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

        self.assertTemplateUsed(response, 'request.html')

    def test_custom_middleware_doesnt_save_getrequests_post(self):
        """ i've decided ignore  request from /request/ page"""
        self.client.get(reverse('index'))

        _count = MyHttpRequest.objects.count()

        self.client.post(reverse('getrequests'))

        self.assertEquals(_count, MyHttpRequest.objects.count())
        self.assertNotEquals(_count, 0)

    def test_get_requests_retuns_not_viewed_request_number(self):
        """ requests number should updates asynchronously """
        self.client.get(reverse('index'))
        response = self.client.get(reverse('getrequests'))
        data = json.loads(response.content)
        self.assertEquals(data['count'], 1)

        self.client.get(reverse('index'))
        response = self.client.get(reverse('getrequests'))
        data = json.loads(response.content)
        self.assertEquals(data['count'], 2)

    def test_requests_count_updates_on_page_reload(self):
        """when /request/ page updates - all myhhtprequest objects sets ridden
        """
        self.client.get(reverse('index'))
        response = self.client.get(reverse('getrequests'))
        self.assertEquals(json.loads(response.content)['count'], 1)

        self.client.get(reverse('request'))
        response = self.client.get(reverse('getrequests'))
        self.assertEquals(json.loads(response.content)['count'], 0)

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
