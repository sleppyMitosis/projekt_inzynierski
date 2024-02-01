import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inz_back.settings')

app = Celery('inz_back')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-medication-emails-everyday': {
        'task': 'medications.tasks.send_medication_reminders',
        'schedule': crontab(hour=19, minute=00),
    },
}

