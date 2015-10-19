import json
from apps.hello.models import MyData
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import EditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def edit_page(request):
    if request.method == 'POST':
        instance = MyData.objects.first()
        form = EditForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            if request.FILES:
                instance.avatar = request.FILES['avatar']

            form.save()
            return HttpResponse(json.dumps(dict(success=True)),
                                content_type='application/json')
        return HttpResponseBadRequest(
            json.dumps(dict(success=True, err_msg=form.errors)),
            content_type='application/json')

    form = EditForm(instance=MyData.objects.first())
    return render(request, 'edit.html', {'form': form})
