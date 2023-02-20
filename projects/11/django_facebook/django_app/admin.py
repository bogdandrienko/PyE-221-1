from django.contrib import admin
from django_app import models


class PostModelExtendAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'PostModel' на панели администратора
    """

    list_display = (
        'author',
        'title',
        'description',
        # 'content',
        'is_moderate',
        'updated',
        'created',
    )
    list_display_links = (
        'author',
        'title',
        'description',
    )
    list_editable = (
        'is_moderate',
    )
    list_filter = (
        'author',
        'title',
        'description',
        # 'content',
        'is_moderate',
        'updated',
        'created',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'author',
            'title',
            'description',
            # 'content',
        )}),
        ('Вспомогательные', {'fields': (
            'is_moderate',
            'updated',
            'created',
        )}),
    )
    search_fields = [
        'author',
        'title',
        'description',
        # 'content',
        'is_moderate',
        'updated',
        'created',
    ]


admin.site.register(models.PostModel, PostModelExtendAdmin)
