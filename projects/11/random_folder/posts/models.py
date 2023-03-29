from django.core.validators import MaxLengthValidator
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=128, validators=[MaxLengthValidator(200)])
    desc = models.TextField()

    def __str__(self):
        return str(self.title)
