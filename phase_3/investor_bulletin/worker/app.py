from celery import Celery
from worker._config import celeryconfig
from worker.schedule.celery_schedule import beat_schedule
# Create a celery app object to start your workers

def create_celery_app():
  app = Celery('asd')
  app.config_from_object(celeryconfig)
  app.conf.beat_schedule = beat_schedule
  app.log.setup_logging_subsystem(loglevel='INFO')
  return app

app = create_celery_app()

if __name__ == '__main__':
  app.start()
