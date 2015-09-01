import json
from django.core import serializers
from django.http import HttpResponse
from .models import MyHttpRequest
from django.shortcuts import render_to_response


def request_view(request, template='request.html'):
    """
    :param request:
    :return: not is_viewed requests_number
    """
    data = MyHttpRequest.objects.all().order_by('-time')[:10]

    for obj in data:
        obj.is_viewed = True
        obj.save()

    requests_count = MyHttpRequest.objects.filter(is_viewed=False).count()

    return render_to_response(template, {'requests_count': requests_count})


def get_requests_view(request):
    """
    :param request:
    :return: 10 last Http Requests from DB
    """
    data = MyHttpRequest.objects.all().order_by('-time')[:10]

    # for obj in data:
    #     obj.is_viewed = True
    #     obj.save()

    data = serializers.serialize('json', data)

    return HttpResponse(data)


def get_requests_count(request):
    """
    :param request:
    :return: not viewed requests count
    """
    data = MyHttpRequest.objects.filter(is_viewed=False).count()

    return HttpResponse(json.dumps(data))
