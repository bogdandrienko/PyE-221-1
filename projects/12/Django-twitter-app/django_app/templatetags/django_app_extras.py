from django import template
import datetime
from django_app import models as django_models

register = template.Library()


@register.filter(name="beatiefy")
def beatiefy(source_string: str, target_length: int):
    if len(source_string) > target_length:
        res = source_string[:target_length] + "..."
    else:
        res = source_string
    return res


@register.simple_tag(takes_context=True)
def beatiefy_tag(context, source_string: str, target_length: int):
    if len(source_string) > target_length:
        res = source_string[:target_length] + "..."
    else:
        res = source_string
    return res


@register.filter(name="digit_beatiefy")
def digit_beatiefy(value):
    src = str(value)
    if 3 < len(src) < 6:
        out = src[3:] + " " + src[0:3]
    elif 6 < len(src) < 9:
        out = src[6:] + " " + src[3:6] + " " + src[0:3]
    elif 9 < len(src) < 12:
        out = src[9:] + " " + src[6:9] + " " + src[3:6] + " " + src[0:3]
    else:
        out = src
    return out


@register.simple_tag(takes_context=True)
def text_upper_case(context, text: str):
    try:
        return str(text).upper()
    except Exception as error:
        print("error simple_tag text_upper_case: ", error)
        return ""


@register.simple_tag(takes_context=True)
def access_tag(context):
    request = context["request"]
    user = request.user
    auth = user.is_authenticated
    return auth


@register.simple_tag(takes_context=True)
def post_my_rating(context, post_id):
    """
    Смотрит, поставил ли я лайк или дизлайк этому посту
    """
    user = context["request"].user
    _post = django_models.PostModel.objects.get(id=post_id)
    return _post.is_user_post_ratings(user)


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.filter(name="cut_string")
def cut_string(value, arg: int):
    return f"{value[0:arg]}..."


@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, "")


@register.filter(name="lower")
def lower(value):
    return value.lower()
