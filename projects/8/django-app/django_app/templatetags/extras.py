from django import template
from django.contrib.auth.models import User, Group

register = template.Library()


@register.filter(name='check_odd_filter')
def check_odd_filter(value):
    return int(value) % 2 == 0
    # try:
    #
    # except Exception as error:
    #     print(error)
    #     return 'error'


@register.simple_tag(takes_context=True)
def slice_string(context, text: str, length: int):
    request = context["request"]
    # user = request.user
    #
    # groups = Group.objects.all()
    #
    # user

    user = User.objects.get(username=request.user.username)

    return text[0:length:1]


@register.simple_tag(takes_context=True)
def is_glavvarch(context, text: str, length: int):
    # request = context["request"]
    # request = context.get('request', None)
    # print(request)
    # request.Post
    # request.data
    # request.data
    # user = request.user
    # users = User.objects.all()  # получить всех пользователей системы
    # users_with_groups = []
    # for user in users:
    #     users_with_groups.append(
    #         {"user": user, "groups": Group.objects.filter(user=user)}
    #     )
    # [
    #     {"user": user1, "groups": []},
    #     {"user": user2, "groups": [Group.objects.filter(user=user)]},
    #     {"user": user3, "groups": Group.objects.filter(user=user)},
    #     {"user": user, "groups": Group.objects.filter(user=user)},
    #     {"user": user, "groups": Group.objects.filter(user=user)},
    #     {"user": user, "groups": Group.objects.filter(user=user)},
    # ]
    #
    groups = Group.objects.all()
    #
    # user

    # user = User.objects.get(username=request.user.username)

    return text[0:length:1]
