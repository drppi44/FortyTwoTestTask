import json
from django.core import serializers
from django.core.urlresolvers import reverse
from .views import get_requests
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

        # self.client.post('/request/ajax/getrequests/')
        self.client.post(reverse('getrequests'))

        self.assertEquals(_count, MyHttpRequest.objects.count())
        self.assertNotEquals(_count, 0)

    def test_getrequest_marks_its_objects_as_viewed(self):
        """all query_string objects returned by getrequest response
         should be marked as_views=True """
        self.client.get(reverse('index'))
        self.client.get(reverse('request'))

        response = self.client.get(reverse('getrequests'))
        data = json.loads(response.content)

        query_set_of_returned_myhttp_objects = MyHttpRequest.objects.filter(
            id__in=(obj['pk'] for obj in data)
        )

        self.assertTrue(
            all(obj.is_viewed for obj in query_set_of_returned_myhttp_objects)
        )

    def test_requests_number_updates(self):
        """ requests number should updates asynchronously """
        self.client.get(reverse('index'))
        response = self.client.get(reverse('getrequestscount'))
        self.assertEquals(response.content, '1')

        self.client.get(reverse('index'))
        response = self.client.get(reverse('getrequestscount'))
        self.assertEquals(response.content, '2')

    def test_requests_count_updates_on_page_reload(self):
        """when /request/ page updates - all myhhtprequest objects
        sets ridden
        """
        self.client.get(reverse('index'))
        response = self.client.get(reverse('getrequestscount'))
        self.assertEquals(response.content, '1')

        response = self.client.get(reverse('request'))
        self.assertEquals(response.context['requests_count'], 0)

    def test_reqeust_page_shows_exactly_10_last_requests(self):
        """get_requests fn return 10 last request"""
        request = MyHttpRequest()

        for i in range(11):
            self.client.get(reverse('index'))

        response = get_requests(request)
        data = MyHttpRequest.objects.all().order_by('-time')[:10]
        ten_records_from_db = serializers.serialize('json', data)

        self.assertEquals(ten_records_from_db, response.content)

    def test_view_with_empty_db(self):
        """/request/ html renders with empty reqeusts in db"""
        response = self.client.get(reverse('request'))

        self.assertIn('Middleware', response.content)
