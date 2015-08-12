import json
from django.core import serializers
from .models import MyHttpRequest
from django.test import TestCase
from django.test.client import RequestFactory, Client


class TestRequestView(TestCase):
    """ Test class for t3_middleware app
    include tests: save request to db, show it on page,
     update page asynchronously
    """
    pass

    def test_save_request_to_db(self):
        """
        each request should be saved in db
        """
        factory = RequestFactory()

        request = factory.get('/')

        client = Client()
        client.get('/')

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
        response = self.client.get('/request/')

        self.assertTemplateUsed(response, 'request.html')

    def test_custom_middleware_doesnt_save_getrequests_post(self):
        """i've decided not to save post request from javascript on
        requests page"""
        self.client.get('/')

        _count = MyHttpRequest.objects.count()

        self.client.post('/request/ajax/getrequests/')

        self.assertEquals(_count, MyHttpRequest.objects.count())
        self.assertNotEquals(_count, 0)

    def test_getrequest_marks_its_objects_as_viewed(self):
        self.client.get('/')
        self.client.get('/requests/')

        response = self.client.get('/request/ajax/getrequests/')
        print str(response)
