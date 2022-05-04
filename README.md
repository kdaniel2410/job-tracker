# Shift Tracker

## docker-compose.yml

```yaml
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
    labels:
      - "traefik.http.routers.job_tracker.rule=Host(`132.145.76.70`)"
  reverse-proxy:
    image: traefik:v2.6
    command: --providers.docker
    ports:
      - "80:80"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```
