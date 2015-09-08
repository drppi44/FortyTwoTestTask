from apps.hello.views import index_view
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index_view, name='index'),
    url(r'^request/', include('apps.t3middleware.urls')),

    url(r'^login/$', 'apps.t5edit.views.login_page', name='login'),
    url(r'^edit/', 'apps.t5edit.views.edit_page', name='edit'),

    url(r'^admin/', include(admin.site.urls)),
)
