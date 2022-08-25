FROM python:3.9.13-slim-bullseye as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# `builder-base` STAGE is used to build deps + create our virtual environment
FROM python-base as builder-base
ARG MODE
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml build-poetry.sh ./
RUN apt-get update && \
    apt-get install --no-install-recommends -y git curl build-essential gcc g++ libpq-dev && \
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN ./build-poetry.sh

# `production` image used for runtime
FROM python-base as runner

COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
WORKDIR /usr/code/src
RUN addgroup --system user && \
    adduser --system --no-create-home --group user && \
    chown -R user:user /usr/code && chmod -R 755 /usr/code
COPY ./src /usr/code/src
COPY start-server.sh /usr/code/start-server.sh
RUN chmod +x /usr/code/start-server.sh

CMD ["/usr/code/start-server.sh"]
