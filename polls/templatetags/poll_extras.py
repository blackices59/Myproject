from django import template

register = template.Library()


def cut(value, arg):
    return value.replace(arg, '')


def lower(value):
    return value.lower()
