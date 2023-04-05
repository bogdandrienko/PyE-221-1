from django.contrib.auth.models import User
from django_app import models as django_models


def user_count(request):
    try:
        count = User.objects.all().count()
    except Exception as error:
        print("error: ", error)
        count = 0
    return dict(user_count=count)


def post_count(request):
    try:
        count = django_models.PostModel.objects.all().count()
    except Exception as error:
        print("error: ", error)
        count = 0
    return dict(post_count=count)
