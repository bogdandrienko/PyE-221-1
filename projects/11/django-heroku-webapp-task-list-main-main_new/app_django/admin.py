from django.contrib import admin
from . import models


# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Task' на панели администратора
    """

    list_display = (
        'author',
        'title',
        'description',
        'is_completed',
        'created',
        'updated'
    )
    list_display_links = (
        'title',
        'description',
    )
    list_editable = (
        'is_completed',
    )
    list_filter = (
        'author',
        'title',
        'description',
        'is_completed',
        'created',
        'updated'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'author',
            'title',
            'description',
            'is_completed',
            'created',
            'updated'
        )}),
    )
    search_fields = [
        'author',
        'title',
        'description',
        'is_completed',
        'created',
        'updated'
    ]


admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Post)
admin.site.register(models.PostComment)
admin.site.register(models.PostLike)
