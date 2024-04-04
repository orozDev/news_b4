from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def template_mark_safe(val):
    return mark_safe(val)
