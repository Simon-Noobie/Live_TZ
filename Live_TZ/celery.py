import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Live_TZ.settings')

app = Celery('Live_TZ')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

