#!/bin/bash
# celery.sh

celery -A app beat -l debug &
celery -A app worker -l info &
