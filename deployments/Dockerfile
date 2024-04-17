FROM python:3.12-alpine3.19

LABEL maintainer="admin@example.com"

# Prevent python to buffer outputs and prints them directly to the console.
ENV PYTHONUNBUFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG C.UTF-8
ENV TZ="UTC"

# For venv:
# COPY ./requirements/ /tmp/
COPY . /app/
WORKDIR /app
EXPOSE 8000

ARG ENVIRONMENT=production

# # For venv:
# RUN python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     apk add --update --no-cache postgresql-client && \
#     apk add --update --no-cache --virtual .tmp-build-deps \
#         build-base postgresql-dev musl-dev && \
#     /py/bin/pip install -r /tmp/requirements.txt && \
#     if [ "$ENVIRONMENT" = "development" ]; \
#         then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
#     fi && \
#     rm -rf /tmp && \
#     apk del .tmp-build-deps && \
#     adduser \
#         --disabled-password \
#         --no-create-home \
#         django-user

# For pipenv:
  RUN pip3 install --no-cache-dir --upgrade pipenv && \
    # The next 3 lines are for installing postgres adapter
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
      build-base postgresql-dev musl-dev && \
    if [ "$ENVIRONMENT" = "development" ]; \
      then pipenv install --dev --system ; \
      else pipenv install --system ; \
    fi && \
    pip3 install --no-cache-dir psycopg2 && \
    rm -rf /tmp && \
    rm -rf get-pip.py && \
    apk del .tmp-build-deps && \
    adduser \
      --disabled-password \
      --no-create-home \
      django-user

# For venv:
# ENV PATH="/py/bin:$PATH"

USER django-user
