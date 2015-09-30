from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import urlize as urlize_impl

register = template.Library()

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def urlize_target_blank(value):
    return mark_safe(urlize_impl(value).replace('<a', '<a target="_blank"'))
