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


class LogAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'LogModel' на панели администратора
    """

    list_display = (
        'user',
        'method',
        'status',
        'url',
        'description',
        'level',
        'datetime',
    )
    list_display_links = (
        'user',
        'method',
        'status',
        'url',
    )
    list_editable = (
        'level',
    )
    list_filter = (
        'user',
        'method',
        'status',
        'url',
        'description',
        'datetime',
        'level',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'user',
            'method',
            'status',
            'url',
            'description',
            'datetime',
            'level',
        )}),
    )
    search_fields = [
        'user',
        'method',
        'status',
        'url',
        'description',
        'datetime',
        'level',
    ]


admin.site.register(models.LogModel, LogAdmin)
