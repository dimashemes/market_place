#!/bin/sh

export DJANGO_SETTINGS_MODULE=shop.settings

python manage.py collectstatic --noinput

echo 'Applying migrations...'
python manage.py migrate

gunicorn shop.wsgi:application --bind 0.0.0.0:$PORT
