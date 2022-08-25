#!/bin/bash

if [ "$MODE" != "DEVELOPMENT" ]
then
  poetry install --no-dev
else
  poetry install
fi
