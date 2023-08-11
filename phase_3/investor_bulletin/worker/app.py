from celery import Celery
from worker._config import celeryconfig
from worker.schedule.celery_schedule import beat_schedule
# Create a celery app object to start your workers

def create_celery_app(name, broker_url):
  return Celery(name, broker=broker_url)

app = create_celery_app('napp', 'amqp://localhost')
app.conf.beat_schedule = beat_schedule
app.log.setup_logging_subsystem(loglevel='INFO')

from tasks import celery_tasks
if __name__ == '__main__':
  app.start()
