from apps.hello.models import UserProfile, Task
from apps.hello.widgets import DatePickerWidget
from crispy_forms.layout import Submit
from django import forms
from crispy_forms.helper import FormHelper


class EditForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DatePickerWidget(
        params="{dateFormat: 'yy-mm-dd', changeYear: true,"
               " defaultDate: 'c-20', yearRange: 'c-100:c'}",
        attrs={'class': 'datepicker'}))

    class Meta:
        model = UserProfile
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5, 'cols': 25}),
            'other_contacts': forms.Textarea(attrs={'rows': 5, 'cols': 25}),
        }


class TaskForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

    class Meta:
        model = Task
        fields = ('title', 'description', 'status')
