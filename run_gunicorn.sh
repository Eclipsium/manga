#!/bin/bash

# Change to project directory
cd /home/manga/manga/

/usr/bin/pipenv run gunicorn --daemon -b 92.63.105.56:8000 manga.wsgi:application \
  --name "django-project" \
  --workers 4 \
  --user=root --group=root \
  --bind 127.0.0.1:8000 \
  --log-level=info \
  --log-file="/home/manga/log/gunicorn.logs"
