#!/bin/bash

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Applying database migrations..."
python3 manage.py migrate
