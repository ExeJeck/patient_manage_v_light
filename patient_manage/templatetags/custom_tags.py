from django import template

register = template.Library()

@register.filter
def model_name(obj):
    return obj._meta.object_name


@register.filter
def attr(obj, field_name):
    return getattr(obj, field_name, '')
