FROM python:3.11.4-slim

COPY ./worker/beat-scheduler/entrypoint.sh /usr/local/bin/

RUN apt-get update && apt-get install -y netcat-openbsd

RUN chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /worker/beat-scheduler

COPY ./worker/beat-scheduler .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["entrypoint.sh", "broker"]

CMD ["celery", "-A", "beat_app", "beat", "-l", "info"]
