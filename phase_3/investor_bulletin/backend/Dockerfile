FROM python:3.11.4-slim

COPY ./backend/entrypoint.sh /usr/local/bin/

RUN apt-get update && apt-get install -y netcat-openbsd

RUN chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /app

COPY ./backend .

RUN mkdir -p ./schema-library/dist

COPY ./schema-library/dist ./schema-library/dist

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["entrypoint.sh", "database"]

CMD ["python", "api/main.py"]
