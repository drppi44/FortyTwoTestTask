from apps.hello.views import index_view
from apps.t3_middleware.views import get_requests_view
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index_view, name='index'),
    url(r'^request/', include('apps.t3_middleware.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
