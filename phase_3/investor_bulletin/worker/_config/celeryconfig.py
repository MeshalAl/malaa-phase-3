name = 'app'
broker_url = 'amqp://localhost'
result_backend = 'rpc://localhost'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
imports = ('tasks.celery_tasks', )
timezone = 'Asia/Riyadh'
enable_utc = True
