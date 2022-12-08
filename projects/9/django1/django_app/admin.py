from django.contrib import admin

from django_app import models


class ProductAdmin(admin.ModelAdmin):
    """ """

    list_display = (
        "label",
        "amount",
        "not_bubble_price",
        "bubble_percentage",
        "final_price",
        "vat_price",
        "overall",
    )
    list_display_links = ("label",)
    list_editable = ("amount",)
    list_filter = (
        "label",
        "amount",
        "not_bubble_price",
        "bubble_percentage",
        "final_price",
        "vat_price",
        "overall",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "label",
                    "amount",
                    "not_bubble_price",
                    "bubble_percentage",
                    "final_price",
                    "vat_price",
                    "overall",
                )
            },
        ),
    )
    search_fields = [
        "label",
        "amount",
        "not_bubble_price",
        "bubble_percentage",
        "final_price",
        "vat_price",
        "overall",
    ]


# admin.site.register(models.Product)
admin.site.register(models.Product, ProductAdmin)
