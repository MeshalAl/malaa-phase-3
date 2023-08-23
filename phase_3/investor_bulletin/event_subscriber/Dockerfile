FROM python:3.11.4-slim

COPY ./event_subscriber/entrypoint.sh /usr/local/bin/

RUN apt-get update && apt-get install -y netcat-openbsd

RUN chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /app

COPY ./event_subscriber .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["entrypoint.sh", "broker"]

CMD ["python", "main.py"]
