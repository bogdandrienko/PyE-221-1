from django.contrib import admin
from django_api import models


# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'user_id',
        'title',
        'completed',
    )
    list_display_links = (
        'user_id',
        'title',
    )
    list_editable = (
        'completed',
    )
    list_filter = (
        'user_id',
        'title',
        'completed',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'user_id',
            'title',
            'completed',
        )}),
    )
    search_fields = [
        'user_id',
        'title',
        'completed',
    ]


admin.site.register(models.Todo, TodoAdmin)
