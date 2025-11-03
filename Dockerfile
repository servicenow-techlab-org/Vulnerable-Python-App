# We need a golang build environment first
FROM python:3.9-slim-bookworm

WORKDIR /app
ADD app.py /app
RUN pip3 install Flask

LABEL org.opencontainers.image.source="https://github.com/jonashackt/docker-hello-world"

CMD ["python3", "app.py"]
