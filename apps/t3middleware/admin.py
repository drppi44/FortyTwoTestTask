from .models import MyHttpRequest
from django.contrib import admin


class MyHttpRequestAdmin(admin.ModelAdmin):
    list_display = ('uri', 'is_viewed')


admin.site.register(MyHttpRequest, MyHttpRequestAdmin)
