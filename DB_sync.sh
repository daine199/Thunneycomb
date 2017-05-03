#!/usr/bin/env bash
# -*- coding: utf-8 -*-

python manage.py makemigrations home
python manage.py makemigrations pet_api
python manage.py makemigrations thunder_token
python manage.py makemigrations platycodon

python manage.py migrate
python manage.py migrate home
python manage.py migrate pet_api
python manage.py migrate thunder_token
python manage.py migrate platycodon
