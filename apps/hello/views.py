from .models import MyData
from django.shortcuts import render


def index_view(request, template='index.html'):
    data = MyData.objects.first()
    return render(request, template, {'data': data})
