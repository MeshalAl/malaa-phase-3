from celery.schedules import crontab
from worker.app import app
import worker.tasks.celery_tasks

app.conf.beat_schedule = {
    'run publish alerts every minute': {
        'task': 'worker.tasks.celery_tasks.publish_alerts_task',
        'schedule': crontab(),
        'args': (16, 16),
    },
}
