import json
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import MyHttpRequest, UserProfile
from .forms import EditForm
from . import signals  # noqa


def index_view(request, template='index.html'):
    data = UserProfile.objects.first()
    return render(request, template, {'data': data})


def request_view(request, template='request.html'):
    MyHttpRequest.objects.update(is_viewed=True)

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


@login_required()
def edit_page(request):
    if request.method == 'POST' and request.is_ajax():
        instance = UserProfile.objects.first()
        form = EditForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            if request.FILES:
                instance.avatar = request.FILES['avatar']

            form.save()
            return HttpResponse(json.dumps(dict(success=True)),
                                content_type='application/json')
        return HttpResponseBadRequest(
            json.dumps(dict(success=False, err_msg=form.errors)),
            content_type='application/json')

    form = EditForm(instance=UserProfile.objects.first())
    return render(request, 'edit.html', {'form': form})
