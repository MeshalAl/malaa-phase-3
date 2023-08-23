from celery import Celery
from _config import celery_config
# Create a celery app object to start your workers

def create_celery_app():
  app = Celery('celery_app')
  app.config_from_object(celery_config)
  # app.log.setup_logging_subsystem(loglevel='INFO')
  return app

app = create_celery_app()

if __name__ == '__main__':
  app.start()
