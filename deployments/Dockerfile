FROM python:3.12-slim

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

# For venv:
# RUN python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     /pip/bin/pip install -r /tmp/requirements.txt && \
#     if [ $DEV - "true" ]; \
#         then /py/bin/pip install -r /tmp/requirements_dev.txt ; \
#     fi && \
#     rm -rf /tmp && \
#     adduer \
#         --disabld-password \
#         --no-create-home \
#         django-user

# For pipenv:
RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --upgrade pip && \
    pip3 install pipenv && \
    pipenv lock --clear && \
    if [ "$ENVIRONMENT" = "develpment" ]; \
      then pipenv install --dev --system ; \
      else pipenv install --system ; \
    fi && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# For venv:
# ENV PATH="/py/bin:$PATH"

USER django-user
