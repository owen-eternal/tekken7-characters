FROM python:3.13.0a3-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir -r /tmp/requirements.txt \
  && rm -rf /tmp/requirements.txt \
  && useradd -U app_user \
  && install -d -m 0755 -o app_user -g app_user /app/staticfiles

WORKDIR /app
USER app_user:app_user
COPY --chown=app_user:app_user . .
RUN python manage.py collectstatic --no-input

CMD python3 manage.py migrate && \
    python3 manage.py createsuperuser --no-input && \
    gunicorn \
        --reload \
        --bind 0.0.0.0:8000 \ 
        --workers 2 \
        --log-level DEBUG \
        --access-logfile "-" \
        --error-logfile "-" \
        core.wsgi:application