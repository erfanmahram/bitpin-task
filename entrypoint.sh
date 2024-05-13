#!/bin/bash

python manage.py collectstatic --noinput
python3 manage.py migrate --no-input
gunicorn --config gunicorn-cfg.py core.wsgi
