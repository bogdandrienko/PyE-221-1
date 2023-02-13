import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_settings.settings')
app = Celery('django_settings')
app.config_from_object('django.conf:settings', namespace='CELERY')  # CELERY_Name
app.autodiscover_tasks()

