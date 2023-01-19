import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crs_templates.settings")
app = Celery("crs_templates")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
