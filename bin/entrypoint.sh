#!/usr/bin/env bash

set -e;

APP_GUNICORN_USE=${APP_GUNICORN_USE:-"main.wsgi:application"}
APP_GUNICORN_MAX_REQUESTS=${APP_GUNICORN_MAX_REQUESTS:-"1000"}

APP_GUNICORN_WORKERS_DEFAULT=$(nproc)
APP_GUNICORN_WORKERS=${APP_GUNICORN_WORKERS:-$APP_GUNICORN_WORKERS_DEFAULT}

APP_HOST=${APP_HOST:-"0.0.0.0"}
APP_PORT=${APP_PORT:-"8000"}

# if ! [ -z "$APP_MIGRATE" ]; then
  django-admin migrate --noinput
  django-admin createcachetable
# fi

# if ! [ -z "$APP_COLLECTSTATIC" ]; then
  django-admin collectstatic --noinput
# fi

if ! [ -z "$APP_COMMAND" ]; then
  django-admin $APP_COMMAND
  exit
fi

if ! [ -z "$APP_CREATE_SUPERUSER" ]; then
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); bool(User.objects.filter(username='admin').count()) or User.objects.create_superuser('admin', 'admin')" | django-admin shell
fi

if ! [ -z "$APP_FIXTURES" ]; then
  django-admin loaddata $APP_FIXTURES
fi

#django-admin runserver ${APP_HOST}:${APP_PORT}

#if ! [ -z "$APP_DEBUG" ]; then
#  django-admin runserver ${APP_HOST}:${APP_PORT}
#else
gunicorn -b ${APP_HOST}:${APP_PORT} --access-logfile - --capture-output --max-requests $APP_GUNICORN_MAX_REQUESTS -w $APP_GUNICORN_WORKERS $APP_GUNICORN_USE
#fi