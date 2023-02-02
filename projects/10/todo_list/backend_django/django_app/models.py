from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


# Create your models here.

class Todo(models.Model):
    """
    Задачи
    """

    title = models.CharField(
        db_index=True,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default='',
        verbose_name='Заголовок',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )

    class Meta:
        app_label = 'django_app'
        ordering = ("-title",)
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self) -> str:
        return f"{self.title} ({self.id})"
