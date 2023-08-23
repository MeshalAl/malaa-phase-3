from celery.schedules import crontab
from datetime import timedelta
beat_schedule = {
    'Run pusblish alerts every 5 minutes': {
        'task': 'tasks.celery_tasks.publish_alerts_task',
        'schedule': crontab(),
        'args': (),
    },
    'ping 10 seconds': {
    'task': 'tasks.celery_tasks.ping',
    'schedule': timedelta(seconds=10),
    'args': (),
    },
}
