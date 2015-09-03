from apps.hello.views import index_view
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index_view, name='index'),
    url(r'^request/', include('apps.t3_middleware.urls')),
    url(r'^login/', 'apps.t5_edit.views.login_page', name='login'),

    url(r'^admin/', include(admin.site.urls)),
)
