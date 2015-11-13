from apps.hello.models import MyHttpRequest


class CustomMiddleware(object):
    @staticmethod
    def process_response(request, response):
        kwargs = dict(
            host=request.get_host(),
            path=request.path,
            method=request.META['REQUEST_METHOD'],
            uri=request.build_absolute_uri(),
            query_string=request.META['QUERY_STRING'],
            status_code=response.status_code
        )
        if not request.is_ajax() and 'jsi18n' not in kwargs['uri']:
            MyHttpRequest.objects.create(**kwargs)
        return response
