#!/bin/bash

LAST_PYTHON_VERSION=$(find /usr/bin -name 'python*' | grep -E '^/usr/bin/python[0-9]+(\.[0-9]+)?$' | sed 's|/usr/bin/||' | sort -V | tail -n 1)

if [ -z "$LAST_PYTHON_VERSION" ]; then
    echo "No version of Python was found in directory /usr/bin. Please, install it and try again."
    exit 1
fi

is_integer() {
    [[ "$1" =~ ^-?[0-9]+$ ]]
}

if ! is_integer "$1" || ! is_integer "$2"; then
    echo "The parameters are not valid."
    exit 1
fi

cd backend/tests

$LAST_PYTHON_VERSION api-stress-test.py $1 $2