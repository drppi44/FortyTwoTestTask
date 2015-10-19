from .models import MyHttpRequest


class CustomMiddleware(object):
    @staticmethod
    def process_request(request):
        kwargs = {
            'host': request.get_host(),
            'path': request.path,
            'method': request.method,
            'uri': request.build_absolute_uri(),
            'query_string': request.META['QUERY_STRING']
        }

        if 'request' not in kwargs['uri'] and 'jsi18n' not in kwargs['uri']:
            MyHttpRequest.objects.create(**kwargs)
