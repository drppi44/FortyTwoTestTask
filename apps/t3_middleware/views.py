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
    data = MyHttpRequest.objects.all().order_by('-time')[:10]

    for obj in data:
        obj.is_viewed = True
        obj.save()

    data = serializers.serialize('json', data)

    return HttpResponse(data)
