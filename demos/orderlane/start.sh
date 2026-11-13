#!/usr/bin/env sh
set -eu
cd demos/orderlane
python manage.py migrate --noinput
exec gunicorn config.wsgi:application --bind "0.0.0.0:$PORT" --workers 1 --threads 2 --timeout 30 --access-logfile - --error-logfile -
