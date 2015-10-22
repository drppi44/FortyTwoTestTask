from django.contrib import admin
from .models import MyData, ModelSignal


class MyDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(MyData, MyDataAdmin)
admin.site.register(ModelSignal)
