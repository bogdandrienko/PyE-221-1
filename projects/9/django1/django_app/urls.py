from django.urls import path

from django_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("create/", views.create, name="create"),
    path("import_data/", views.import_data, name="import_data"),
    path("export_data/", views.export_data, name="export_data"),
]
