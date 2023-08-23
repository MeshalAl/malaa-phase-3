#!/bin/sh
# entrypoint.sh

set -e

host="$1"
shift
cmd="$@"

until nc -z -v -w30 $host 26257; do
  echo "CockroachDB is unavailable - sleeping"
  sleep 1
done

echo "CockroachDB is up - executing command"
exec $cmd
