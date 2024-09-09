#!/bin/bash

install_frontend() {
    if command -v pnpm >/dev/null 2>&1; then
        echo "pnpm found. Installing dependencies..."
        echo " "
        pnpm install
    elif command -v yarn >/dev/null 2>&1; then
        echo "yarn found. Installing dependencies..."
        echo " "
        yarn install
    elif command -v npm >/dev/null 2>&1; then
        echo "npm found. Installing dependencies..."
        echo " "
        npm install
    else
        echo "No package manager was found (pnpm, yarn or npm). Please, install of them and try again."
        echo " "
        exit 1
    fi
}

install_backend() {
    if command -v poetry >/dev/null 2>&1; then
        echo "poetry found. Installing dependencies..."
        echo " "
        poetry install
    else
        echo "Poetry not found. Please, install it and try again."
        echo " "
        exit 1
    fi
}

cd backend
install_backend

cd ../frontend
install_frontend

cd ..