import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from .models import MyHttpRequest


def request_view(request, template='request.html'):
    MyHttpRequest.objects.filter(is_viewed=False).update(is_viewed=True)

    return render(request, template)


def get_requests(request):
    """ return  10 last Http Requests from DB and not viewed count"""
    ten_requests = MyHttpRequest.objects.all()[:10]
    data = dict(
        count=MyHttpRequest.objects.filter(is_viewed=False).count(),
        text=render_to_string('table_for_requests.html',
                              dict(requests=ten_requests))
    )
    return HttpResponse(json.dumps(data), content_type='application/json')
