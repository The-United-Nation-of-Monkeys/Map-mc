#!/bin/bash

python3 -m alembic upgrade head 

gunicorn app.main:app --workers 4 --timeout 100 --worker-class uvicorn.workers.UvicornWorker --bind="0.0.0.0:8000" &

echo huesos

wait