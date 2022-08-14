FROM python:3.10

ENV POETRY_VERSION=1.1.14
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION
ENV PATH=/root/.local/bin:$PATH

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.in-project true --local
RUN poetry install --no-dev

COPY . .
CMD [ "poetry", "run", "python", "-c", "print('hello world')" ]