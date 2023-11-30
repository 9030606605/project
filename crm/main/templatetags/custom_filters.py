# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def separate_words(value):
    words = value.split('/n')
    return words

