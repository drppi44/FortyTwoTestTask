from apps.hello.models import MyData
from django import forms
from django.forms.extras.widgets import SelectDateWidget


class EditForm(forms.ModelForm):
    class Meta:
        model = MyData
        widgets = {
            'date_of_birth': SelectDateWidget(years=range(1920, 2015))
        }
