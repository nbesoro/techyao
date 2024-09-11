#!/bin/bash

python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:8005