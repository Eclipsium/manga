from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manga.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault('C_FORCE_ROOT', 'true')

# app = Celery('manga_api',
#              broker='amqp://manga:mangapassword@localhost:5672/mangahost',
#              )
#
app = Celery('manga_api',
             broker='redis://localhost:6379/0',
             )

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

