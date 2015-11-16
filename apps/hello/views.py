import json
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.hello.models import MyHttpRequest, UserProfile, Task
from apps.hello.forms import EditForm, TaskForm
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
import signals  # noqa


def index_view(request, template='hello/index.html'):
    data = UserProfile.objects.first()
    return render(request, template, {'data': data})


def request_view(request, template='hello/request.html'):
    return render(request, template)


def get_requests(request):
    """ return 10 last Http Requests from DB and not viewed count"""
    ten_requests = MyHttpRequest.objects.all()[:10]
    data = dict(
        count=MyHttpRequest.objects.filter(is_viewed=False).count(),
        text=render_to_string('hello/table_for_requests.html',
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
    return render(request, 'hello/edit.html', {'form': form})


def update_requests(request):
    MyHttpRequest.objects.update(is_viewed=True)
    return HttpResponse()


class TaskListView(ListView):
    context_object_name = "task_list"
    template_name = 'hello/task.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskListView, self).dispatch(*args, **kwargs)


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'hello/task_create.html'
    success_url = '/task/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskCreateView, self).dispatch(*args, **kwargs)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'hello/task_create.html'
    success_url = '/task/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)
