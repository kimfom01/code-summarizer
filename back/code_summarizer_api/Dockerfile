FROM python:3.11-slim AS release
EXPOSE 5000

WORKDIR /app

ENV POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl make \
    && curl -sSL https://install.python-poetry.org | python - \
    && apt-get clean

RUN poetry config virtualenvs.create false

COPY pyproject.toml .

COPY poetry.lock .

RUN poetry install

COPY . .

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]