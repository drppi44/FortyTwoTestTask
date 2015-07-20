from django.shortcuts import render_to_response
from .models import MyData


def index_view(request, template='index.html'):
    data = MyData.objects.all().first()
    return render_to_response(template, {'data': data})
