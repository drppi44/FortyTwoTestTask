from django.core.urlresolvers import reverse
from django import template

register = template.Library()


@register.simple_tag
def url_to_edit_object(obj):
    url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                          obj._meta.module_name),
                  args=[obj.id])
    return url
