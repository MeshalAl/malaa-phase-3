from os import environ

broker_url = environ.get('BROKER_URL')
result_backend = environ.get('RESULTS_URL')
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
imports = ('tasks.celery_tasks', )
timezone = 'Asia/Riyadh'
enable_utc = True
