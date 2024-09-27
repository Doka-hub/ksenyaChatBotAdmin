from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KseniyaChatBotAdmin.settings')

app = Celery('KseniyaChatBotAdmin')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    broker_url='redis://redis:6379/0',
    result_backend='redis://redis:6379/0',
    broker_connection_retry_on_startup=True,
)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
