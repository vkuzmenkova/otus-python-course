import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoo.settings')

celery_app = Celery('zoo', result_backend="rpc://")
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(packages=None)
