from django.db import models


# Create your models here.


class Todo(models.Model):  # TODO таблица в базе данных
    """
    # Object Relative Model ORM
    # Structured Query Lang...
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/
    """

    # id = models.BigAutoField, autoincrement

    user = models.IntegerField(  # TODO поле в этой таблице
        verbose_name="user",
        default=0,
        editable=True,
        blank=True
    )
    title = models.CharField(
        verbose_name="title",
        default="",
        editable=True,
        blank=True,

        max_length=300  # TODO свойство(параметр) этого поля
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        # db_table

    def __str__(self):
        return f"Todo: {self.title} ({self.user}) [{self.id}]"
