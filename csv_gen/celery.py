from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_gen.settings')

app = Celery('csv_gen')

# class CeleryConfig:
#     task_serializer = "pickle"
#     result_serializer = "pickle"
#     event_serializer = "json"
#     accept_content = ["application/json", "application/x-python-serialize"]
#     result_accept_content = ["application/json", "application/x-python-serialize"]


# app.config_from_object(CeleryConfig)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# appc.config_from_object(CeleryConfig)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
