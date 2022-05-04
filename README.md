# Shift Tracker

## docker-compose.yml

```
services:
  postgres:
    container_name: postgres
    image: postgres
    volumes:
      - /etc/docker/postgres:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
  job_tracker:
    container_name: job_tracker
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    image: job_tracker
    ports:
      - "8000:8000"
    environment:
      - SECRET_KEY=YOUR-SECRET-KEY
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    depends_on:
      - db

```
