from django.contrib import admin
from django.urls import path, include
from django_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    # path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', views.home, name=''),

    path('', include("django_app.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
