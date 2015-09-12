import json
from apps.hello.models import MyData
from django.http import HttpResponse
from .forms import EditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def login_page(request):
    if request.user.is_authenticated():
        return redirect('/edit/')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('/edit/')

        return redirect('/login/')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def edit_page(request):
    if request.method == 'POST':
        instance = MyData.objects.first()
        form = EditForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            if request.FILES:
                instance.avatar = request.FILES['avatar']
            form.save()
            return HttpResponse(json.dumps('ok'))

    form = EditForm(instance=MyData.objects.first())
    return render(request, 'edit.html', {'form': form})
