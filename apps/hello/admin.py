from django.contrib import admin
from apps.hello.models import UserProfile, ModelSignal, MyHttpRequest


class MyHttpRequestAdmin(admin.ModelAdmin):
    list_display = ('uri', 'is_viewed')


admin.site.register(MyHttpRequest, MyHttpRequestAdmin)
admin.site.register(UserProfile)
admin.site.register(ModelSignal)
