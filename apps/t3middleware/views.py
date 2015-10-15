import json
from django.core import serializers
from django.http import HttpResponse
from .models import MyHttpRequest
from django.shortcuts import render_to_response


def request_view(request, template='request.html'):
    MyHttpRequest.objects.filter(is_viewed=False).update(is_viewed=True)

    return render_to_response(template, {'requests_count': 0})


def get_requests(request):
    """ return  10 last Http Requests from DB """
    data = MyHttpRequest.objects.all().order_by('-time')[:10]

    data = serializers.serialize('json', data)

    return HttpResponse(data)


def get_requests_count(request):
    """ return not viewed requests count """
    data = MyHttpRequest.objects.filter(is_viewed=False).count()

    return HttpResponse(json.dumps(data))