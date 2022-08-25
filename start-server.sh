#!/bin/bash

if [ "$ENVIRONMENT" != "DEVELOPMENT" ]
then
    gunicorn -w 2 'main:app'
else
    python main.py
fi

exec "$@"
