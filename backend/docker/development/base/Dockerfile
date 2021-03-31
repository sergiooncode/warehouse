FROM python:3.9.2-alpine

COPY . /warehouse-backend

WORKDIR /warehouse-backend

RUN apk update && \
    apk add gcc \
    build-base \
    linux-headers \
    openssl-dev \
    musl-dev \
    python3-dev \
    libffi-dev \
    bash

RUN pip install --upgrade pip

COPY ./pyproject.toml /warehouse-backend/pyproject.toml
COPY ./poetry.lock /warehouse-backend/poetry.lock

RUN CRYPTOGRAPHY_DONT_BUILD_RUST=1 pip install poetry
RUN POETRY_VIRTUALENVS_CREATE=false poetry install