from django.contrib import admin
from .models import MyData


class MyDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(MyData, MyDataAdmin)
