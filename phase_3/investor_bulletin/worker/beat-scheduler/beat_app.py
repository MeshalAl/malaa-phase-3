from celery import Celery
from _config import celery_config
from schedule.celery_schedule import beat_schedule

def create_celery_app():
  app = Celery('beat_app')
  app.config_from_object(celery_config)
  app.conf.beat_schedule = beat_schedule
  app.log.setup_logging_subsystem(loglevel='INFO')
  return app

app = create_celery_app()

if __name__ == '__main__':
  app.start()
