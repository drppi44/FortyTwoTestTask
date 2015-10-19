from apps.t3middleware.views import request_view
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', request_view, name='request'),

    # ajax
    url(r'ajax/getrequests/$', 'apps.t3middleware.views.get_requests',
        name='getrequests'),
)
