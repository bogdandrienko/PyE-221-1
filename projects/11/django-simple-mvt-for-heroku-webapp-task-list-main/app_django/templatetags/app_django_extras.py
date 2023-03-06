from django import template
import datetime

from app_django import models

register = template.Library()


@register.simple_tag(takes_context=True)
def text_upper_case(context, text: str):
    try:
        return str(text).upper()
    except Exception as error:
        print("error simple_tag text_upper_case: ", error)
        return ""


@register.simple_tag(takes_context=True)
def access_tag(context, slug: str):
    try:
        return True
    except Exception as error:
        print("error simple_tag access_tag: ", error)
        return True


@register.simple_tag(takes_context=True)
def is_my_like(context, pk):
    try:
        return models.Post.objects.get(id=pk).get_this_post_is_like(user=context["request"].user)
    except Exception as error:
        print("error simple_tag is_my_like: ", error)
        return False


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.filter(name='cut_string')
def cut_string(value, arg: int):
    """Removes all values of arg from the given string"""
    return f"{value[0:arg]}..."


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


@register.filter(name='lower')
def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.filter(name='cut_string_50')
def cut_string_50(source):
    if len(source) > 50:
        return source[0:50]
    else:
        return source


@register.simple_tag
def today(is_word):
    if is_word == True:
        now = datetime.datetime.now().weekday() + 1  # TODO get day_off_week by name
        return now
        # print(datetime.datetime.weekday())
    else:
        now = datetime.datetime.now().weekday() + 1
        return now
