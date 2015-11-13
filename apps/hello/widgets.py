from django import forms
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.loader import render_to_string


class DatePickerWidget(forms.DateInput):
    class Media:
        css = {
            'all': (staticfiles_storage.url('css/jquery-ui.css'),)
        }
        js = (
            staticfiles_storage.url('js/jquery-ui.min.js'),
        )

    def __init__(self, params='', attrs=None):
        self.params = params
        super(DatePickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(DatePickerWidget, self).render(name,
                                                        value,
                                                        attrs=attrs)
        rendered_js = render_to_string('hello/date_time_picker_template.html',
                                       dict(name=name, params=self.params))
        return rendered + rendered_js
