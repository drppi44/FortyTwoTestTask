from .models import UserProfile
from .widgets import DatePickerWidget
from django import forms


class EditForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DatePickerWidget(
        params="{dateFormat: 'yy-mm-dd', changeYear: true,"
               " defaultDate: 'c-20', yearRange: 'c-100:c'}",
        attrs={'class': 'datepicker'}))

    class Meta:
        model = UserProfile
