import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTNGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
