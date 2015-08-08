from apps.hello.views import index_view
from apps.t3_middleware.views import request_view, get_requests_view
# from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index_view, name='index'),
    url(r'^request/$', request_view, name='request'),

    # ajax
    url(r'^ajax/getrequests/$', get_requests_view),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': settings.MEDIA_ROOT,
    #      'show_indexes': True}),
)
