from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter
def in_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter
def brutto(value):
    return round((float(value) * 0.23) + float(value), 2)


@register.filter
def to_class_name(value):
    return value.__class__.__name__
