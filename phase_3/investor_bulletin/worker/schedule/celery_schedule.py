from celery.schedules import crontab

beat_schedule = {
    'send alert every 60 seconds': {
        'task': 'tasks.celery_tasks.publish_alerts_task',
        'schedule': crontab(),
        'args': (),
    },
    'ping 10 seconds': {
    'task': 'tasks.celery_tasks.ping',
    'schedule': crontab(),
    'args': (),
    },
}
