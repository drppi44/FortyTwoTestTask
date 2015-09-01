from apps.t3_middleware.views import request_view, get_requests_view
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', request_view, name='request'),

    # ajax
    url(r'ajax/getrequests/$', get_requests_view),
)
