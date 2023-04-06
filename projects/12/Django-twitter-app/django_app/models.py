from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone


# Create your models here.


class PostModel(models.Model):
    """
    Модель Поста
    """
    author = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Автор',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',

        to=User,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Заголовок',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    description = models.TextField(
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name='Описание',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )
    is_completed = models.BooleanField(
        editable=True,
        blank=True,
        null=False,
        default=False,
        verbose_name='Статус выполнения',
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    created = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )
    updated = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время обновления',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('-updated', 'title')
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'django_app_post_model_table'

    def __str__(self):
        if self.is_completed:
            completed = "Активно"
        else:
            completed = "Неактивно"
        return f"{self.title}({self.id}) | {self.description[0:30]}... | {completed} | {self.updated}"

    def post_ratings(self):
        """
        Считает лайки и дизлайки для поста по id
        """
        try:
            _rating = PostRatingModel.objects.filter(post=self)
            return {
                "dislikes": _rating.filter(is_like=False).count(),
                "likes": _rating.filter(is_like=True).count()
            }
        except Exception as error:
            return {"dislikes": 0, "likes": 0}

    def is_user_post_ratings(self, user: User) -> int:
        """
        Смотрит, поставил ли я пользователь или дизлайк этому посту
        """
        _rating = PostRatingModel.objects.filter(post=self, user=user)
        if _rating.count() < 1:
            return 0
        else:
            obj = _rating[0]
            if obj.is_like is True:
                return 1
            else:
                return -1

    def get_comments(self):
        """
        Возвращает все комментарии для поста
        """
        return PostCommentModel.objects.filter(post=self)

    def get_comments_count(self):
        """
        Возвращает количество комментариев для поста
        """
        return PostCommentModel.objects.filter(post=self).count()


class PostRatingModel(models.Model):
    """
    Модель Рейтинга Поста
    """
    user = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL,
    )
    post = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пост',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',

        to=PostModel,
        on_delete=models.CASCADE,
    )
    is_like = models.BooleanField(
        editable=True,
        blank=True,
        null=False,
        default=False,
        verbose_name='Рейтинг',
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('-post', 'user')
        verbose_name = 'Лайк поста'
        verbose_name_plural = 'Лайки постов'

    def __str__(self):
        return f"{self.user}({self.id}) | {'Лайкнул' if self.is_like else 'Дизлайкнул'} | {self.post.title}"


class PostCommentModel(models.Model):
    """
    Модель Комментария к Посту
    """
    user = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL,
    )
    post = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пост',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',

        to=PostModel,
        on_delete=models.CASCADE,
    )
    message = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('-created', 'post')
        verbose_name = 'Комментарий поста'
        verbose_name_plural = 'Комментарии постов'

    def __str__(self):
        return f"{self.user}({self.id}) | {self.created} | {self.message[0:20]}... | {self.post.title}"
