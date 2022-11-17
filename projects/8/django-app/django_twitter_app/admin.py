from django.contrib import admin
from django_twitter_app import models


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (  # отображение
        'user',
        'title',
        'description',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'user',
        'title',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке
        'description',
    )
    list_filter = (  # поля для фильтрации
        'user',
        'title',
        'description',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'user',
        'title',
        'description',
    )
    fieldsets = (
        ("Основное", {"fields": ('user', 'title',)}),
        ("Дополнительное", {"fields": ('description',)}),
    )


admin.site.register(models.Post, PostAdmin)  # complex register model
admin.site.register(models.PostComment)  # simple register model
admin.site.register(models.PostRating)  # simple register model
# admin.site.register(models.Post)  # simple register model (no filter / no search)
