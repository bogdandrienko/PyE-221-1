from django.contrib import admin
from django_app import models as django_models

# Register your models here.

admin.site.site_header = '1111111111'  # default: "Django Administration"
admin.site.index_title = '22222222222'  # default: "Site administration"
admin.site.site_title = '333333333'  # default: "Django site admin"


class TodoAdmin(admin.ModelAdmin):
    """
    Settings admin page for Todo
    """
    list_display = (  # отображение
        'user',
        'title',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'user',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке
        'title',
    )
    list_filter = (  # поля для фильтрации
        'user',
        'title',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'user',
        'title',
    )
    fieldsets = (
        ("Основное", {"fields": ('user',)}),
        ("Дополнительное", {"fields": ('title',)}),
    )


admin.site.register(django_models.Todo, TodoAdmin)  # complex register model
# admin.site.register(django_models.Todo)  # simple register model (no filter / no search)
