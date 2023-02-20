# from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class PostModel(models.Model):
    # id = autofield() - AUTOINCREMENT / SERIAL (POSTGRESQL)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=250, unique=True)
    description = models.TextField("Описание")
    # https://lets-code-more.s3.amazonaws.com/static/uploads/2022/09/20/ckeditor.PNG
    # content = RichTextField(config_name='awesome_ckeditor', default="")
    is_moderate = models.BooleanField(default=False)
    updated = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{self.id}]{self.title} {self.description[:50]}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        # table_name...
