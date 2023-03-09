from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание', default="")

    class Meta:
        app_label = 'app_django'
        ordering = ('-title',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        # db_table = 'comment_task_list_model_table'

    def __str__(self):
        return f"{self.title} | {self.description}"

    def pretty(self):
        return f"{self.title}"

    @staticmethod
    def get_by_id(pk: int):
        if pk < 0:
            raise ValueError("value is too small!")
        return Post.objects.get(id=pk)

    def get_this_post_comments(self):
        return PostComment.objects.filter(article=self)

    def get_this_post_comments_count(self) -> int:
        return PostComment.objects.filter(article=self).count()

    def get_this_post_is_like(self, user):
        return len(PostLike.objects.filter(article=self, author=user, status=True)) > 0


class Task(models.Model):
    """
    Модель Task
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    title = models.CharField(
        db_column='title_db_column',
        db_index=True,
        db_tablespace='title_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Заголовок',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    description = models.TextField(
        db_column='description_db_column',
        db_index=True,
        db_tablespace='description_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name='Описание',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )
    is_completed = models.BooleanField(
        db_column='is_completed_db_column',
        db_index=True,
        db_tablespace='is_completed_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=False,
        verbose_name='Статус выполнения',
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    created = models.DateTimeField(
        db_column='created_db_column',
        db_index=True,
        db_tablespace='created_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
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
        db_column='updated_db_column',
        db_index=True,
        db_tablespace='updated_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
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
        app_label = 'app_django'
        ordering = ('-updated',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'task_task_list_model_table'

    def __str__(self):
        if self.is_completed:
            completed = "Активно"
        else:
            completed = "Неактивно"
        return f"{self.title} | {self.description[0:30]}... | {completed} | {self.updated}"


class PostComment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'app_django'
        ordering = ('-date',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'
        # db_table = 'comment_task_list_model_table'

    def __str__(self):
        return f"{self.article} | {self.author} | {self.date} | {self.description}"


class PostLike(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()

    class Meta:
        app_label = 'app_django'
        ordering = ('-id',)
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        db_table = 'like_task_list_model_table'

    def __str__(self):
        return f"{self.article} | {self.author} | {self.status}"


CHOICES = (
    ("1", "DANGER"),
    ("2", "WARNING"),
    ("3", "LIGHT"),
    ("4", "INFO"),
)


class LogModel(models.Model):
    """
    Модель дл хранения как ошибок, так и просто действий пользователя
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, db_index=True)
    method = models.CharField(max_length=7)  # GET POST PUT PATCH OPTIONS HEAD
    status = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(600)])  # GET POST PUT PATCH OPTIONS HEAD
    url = models.CharField(max_length=300, default="")
    description = models.CharField(max_length=500)
    datetime = models.DateTimeField(default=timezone.now, db_index=True)
    # level = models.TextChoices(GEEKS_CHOICES)
    level = models.CharField(max_length=50, choices=CHOICES, default="4")

    class Meta:
        app_label = 'app_django'
        ordering = ('-datetime', 'url')
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
        # db_table = 'log_model_table'

    def __str__(self):
        return f"{self.datetime} | {self.status} | {self.url} | {self.user}"
