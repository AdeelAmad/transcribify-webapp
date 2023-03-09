import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhisperApp.settings')

app = Celery('WhisperApp', broker='redis://:P@55w0rd@66.94.112.250:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()