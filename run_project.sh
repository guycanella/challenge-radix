#!/bin/bash

(cd backend && fastapi dev app/main.py) &

sleep 1

(cd frontend && pnpm run dev) &

sleep 1

xdg-open http://localhost:5173

wait