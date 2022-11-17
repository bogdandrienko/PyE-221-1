from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    # id = models.IntegerField(
    #     verbose_name="user",
    #     default=0,
    #     editable=True,
    #     blank=True
    # )
    user = models.ForeignKey(  # ForeignKey (внешний ключ, вторичный ключ, один ко многим)
        # / OneToOneField (один к одному) / ManyToManyField
        # unique=True,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,  # при удалении записи - SET_NULL (зануляет) CASCADE (удаляется)
        # related_name='user_model',
    )
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=True,
        db_index=True,

        max_length=150
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'django_twitter_app'
        ordering = ('id',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f"Post: {self.title} {self.description[:30]} [{self.id}]"


class PostComment(models.Model):
    # user = models.IntegerField(
    #     verbose_name="user",
    #     default=0,
    #     editable=True,
    #     blank=True
    # )

    user = models.ForeignKey(  # ForeignKey (внешний ключ, вторичный ключ, один ко многим)
        # / OneToOneField (один к одному) / ManyToManyField
        # unique=True,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,  # при удалении записи - SET_NULL (зануляет) CASCADE (удаляется)
        # related_name='user_model',
    )
    article = models.ForeignKey(  # ForeignKey (внешний ключ, вторичный ключ, один ко многим)
        # / OneToOneField (один к одному) / ManyToManyField
        # unique=True,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Статья',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=Post,
        on_delete=models.SET_NULL,  # при удалении записи - SET_NULL (зануляет) CASCADE (удаляется)
        # related_name='user_model',
    )
    text = models.CharField(
        verbose_name="Текст комментария",
        default="",
        editable=True,
        blank=True,
        unique=False,
        db_index=False,

        max_length=300
    )
    created = models.DateTimeField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,  # автоматическое изменение параметра при сохранении модели
        auto_now_add=False,  # автоматическое изменение параметра при добавлении модели
    )

    class Meta:
        app_label = 'django_twitter_app'
        ordering = ('-created',)
        verbose_name = 'Комментарий к публикации'
        verbose_name_plural = 'Комментарии к публикациям'

    def __str__(self):
        return f"PostComment: {self.user} {self.text[:30]} [{self.created}]"


class PostRating(models.Model):
    # TODO ratings
    user = models.ForeignKey(  # ForeignKey (внешний ключ, вторичный ключ, один ко многим)
        # / OneToOneField (один к одному) / ManyToManyField
        # unique=True,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,  # при удалении записи - SET_NULL (зануляет) CASCADE (удаляется)
        # related_name='user_model',
    )
    article = models.ForeignKey(  # ForeignKey (внешний ключ, вторичный ключ, один ко многим)
        # / OneToOneField (один к одному) / ManyToManyField
        # unique=True,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Статья',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=Post,
        on_delete=models.SET_NULL,  # при удалении записи - SET_NULL (зануляет) CASCADE (удаляется)
        # related_name='user_model',
    )
    status = models.BooleanField(
        verbose_name="Статус",
        default=False,
        editable=True,
        blank=True,
        unique=False,
        db_index=False,
    )
    created = models.DateTimeField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,  # автоматическое изменение параметра при сохранении модели
        auto_now_add=False,  # автоматическое изменение параметра при добавлении модели
    )

    class Meta:
        app_label = 'django_twitter_app'
        ordering = ('-created',)
        verbose_name = 'Рейтинг публикации'
        verbose_name_plural = 'Рейтинги публикаций'

    def __str__(self):
        like = "Лайк" if self.status else "Дизлайк"
        return f"PostRating: {self.user} {like} [{self.created}]"
