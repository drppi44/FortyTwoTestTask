from django.shortcuts import render
from .models import MyData


def index_view(request, template='index.html'):
    data = MyData.objects.first()
    return render(request, template, {'data': data})
