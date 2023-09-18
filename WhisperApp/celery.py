import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhisperApp.settings')

app = Celery('WhisperApp', broker='')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
