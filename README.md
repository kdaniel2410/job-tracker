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
  tracker:
    container_name: tracker
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    image: tracker
    ports:
      - "8000:8000"
    environment:
      - SECRET_KEY=YOUR-SECRET-KEY
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    depends_on:
      - postgres
    labels:
      - "traefik.http.routers.tracker.rule=Host(`132.145.76.70`)"
  traefik:
    container_name: traefik
    image: traefik:v2.6
    command: --providers.docker
    ports:
      - "80:80"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```
