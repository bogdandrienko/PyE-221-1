from django.contrib import admin
from django_app import models as django_models


# Register your models here.

admin.site.register(django_models.PostModel)
admin.site.register(django_models.PostRatingModel)
admin.site.register(django_models.PostCommentModel)
