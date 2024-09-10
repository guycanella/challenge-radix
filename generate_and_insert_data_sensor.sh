#!/bin/bash

LAST_PYTHON_VERSION=$(find /usr/bin -name 'python*' | grep -E '^/usr/bin/python[0-9]+(\.[0-9]+)?$' | sed 's|/usr/bin/||' | sort -V | tail -n 1)

if [ -z "$LAST_PYTHON_VERSION" ]; then
    echo "No version of Python was found in directory /usr/bin. Please, install it and try again"
    exit 1
fi

cd backend/app/db

$LAST_PYTHON_VERSION generate_sensor_data.py

if [ -f "data_sensor.dat" ]; then
    $LAST_PYTHON_VERSION insert_sensor_data.py
    echo "Insertion of data in database finished correctly."
else
    echo "Error: file data_sensor.dat was not found. check if generate_sensor_data.py finished correctly."
    exit 1
fi

cd ../../../