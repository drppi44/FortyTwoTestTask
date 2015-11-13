from apps.hello.views import index_view, request_view, get_requests, edit_page
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', index_view, name='index'),

    # /request/
    url(r'^request/$', request_view, name='request'),
    url(r'ajax/getrequests/$', get_requests, name='getrequests'),

    # /edit/
    url(r'^edit/', edit_page, name='edit'),

    # auth
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
    )
