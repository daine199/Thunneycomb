#!/usr/bin/env bash
# -*- coding: utf-8 -*-

python manage.py makemigrations home
python manage.py makemigrations platycodon

python manage.py migrate
