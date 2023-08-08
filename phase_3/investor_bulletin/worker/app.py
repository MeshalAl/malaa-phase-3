from celery import Celery
from worker._config import celeryconfig

# Create a celery app object to start your workers

def create_celery_app(name, broker_url):
  return Celery(name, broker=broker_url)

app = create_celery_app('task', 'amqp://localhost')

if __name__ == '__main__':
  app.start()
