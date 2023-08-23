FROM python:3.11.4-slim

COPY ./worker/entrypoint.sh /usr/local/bin/

RUN apt-get update && apt-get install -y netcat-openbsd

RUN chmod +x /usr/local/bin/entrypoint.sh

COPY ./worker/celery.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/celery.sh

WORKDIR /worker

COPY ./worker .

RUN mkdir -p ./schema-library/dist

COPY ./schema-library/dist ./schema-library/dist

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["entrypoint.sh", "broker"]

CMD ["celery", "-A", "app", "worker"]
