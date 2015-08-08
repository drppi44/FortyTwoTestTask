from apps.hello.views import index_view
from .models import MyHttpRequest
from django.test import TestCase
from django.test.client import RequestFactory, Client


class TestRequestView(TestCase):
    """ Test class for t3_middleware app
    include tests: save request to db, show it on page, update page asynchronously
    """
    pass

    def test_save_request_to_db(self):
        """
        request must be saved in db
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

