# We need a golang build environment first
FROM python:3.9-slim-bookworm
ARG VCS_REF=UNKNOWN
WORKDIR /app
ADD app.py /app
RUN pip3 install Flask

LABEL org.opencontainers.image.source="https://github.com/jonashackt/docker-hello-world" \
      org.opencontainers.image.revision=$VCS_REF

CMD ["python3", "app.py"]
