import json
from django.core import serializers
from django.http import HttpResponse
from .models import MyHttpRequest
from django.shortcuts import render_to_response


def request_view(request, template='request.html'):
    return render_to_response(template, {})


def get_requests_view(request):
    """
    :param request:
    :return: 10 last Http Requests from DB
    """
    _data = MyHttpRequest.objects.all().order_by('-time')[:10]
    data = serializers.serialize('json', _data)
    print data
    return HttpResponse(data)