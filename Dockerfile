FROM python:3.7
LABEL MAINTAINER="Trim21 <Trim21me@gmail.com>"
ENV PYTHONPATH=/
WORKDIR /

RUN pip install -q poetry

COPY ./poetry.lock /poetry.lock
COPY ./pyproject.toml /pyproject.toml

RUN poetry install --no-dev

COPY / /

ARG DAO_COMMIT_SHA
ENV COMMIT_SHA=$DAO_COMMIT_SHA
ARG DAO_COMMIT_TAG
ENV COMMIT_TAG=$DAO_COMMIT_TAG

EXPOSE 8000

CMD gunicorn app.fast:app \
        -w 3 -k uvicorn.workers.UvicornWorker \
        -b 0.0.0.0:8000 --access-logfile -
