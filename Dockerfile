FROM python:3.12-slim

RUN mkdir "app"

WORKDIR /app

COPY requirements.txt .

RUN popd install -r requirements.txt