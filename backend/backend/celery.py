from __future__ import absolute_import, unicode_literals
import os
from .settings import CELERY_BROKER_URL
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend', broker=CELERY_BROKER_URL)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

from datetime import timedelta

app.conf.beat_schedule = {
    'fetch-and-store-data-every-5-minutes': {
        'task': 'battlebit.tasks.fetch_and_store_data',
        'schedule': timedelta(minutes=5),
    },
}
