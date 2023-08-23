#!/bin/bash
# entrypoint.sh

set -e

host="$1"
shift
cmd="$@"

# Wait until RabbitMQ is up and running
until nc -z $host 5672; do
  >&2 echo "RabbitMQ is unavailable - waiting..."
  sleep 1
done

>&2 echo "RabbitMQ is up - executing command"
exec $cmd
