from tasks.celery_tasks import ping

x = ping.delay().get()
print(x)
