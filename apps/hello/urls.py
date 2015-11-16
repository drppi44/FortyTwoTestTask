from apps.hello.views import TaskCreateView, TaskListView, TaskUpdateView
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'apps.hello.views.index_view', name='index'),

    # /request/
    url(r'^request/$', 'apps.hello.views.request_view', name='request'),
    url(r'ajax/getrequests/$', 'apps.hello.views.get_requests',
        name='getrequests'),
    url(r'ajax/request/update/$', 'apps.hello.views.update_requests',
        name='updaterequests'),

    # /edit/
    url(r'^edit/', 'apps.hello.views.edit_page', name='edit'),

    # /task/
    url(r'^task/$', TaskListView.as_view(), name='task'),
    url(r'^task/add$', TaskCreateView.as_view(), name='task_create'),
    url(r'^task/(?P<pk>[0-9]+)/$', TaskUpdateView.as_view(),
        name='task_update'),

    # auth
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
)
