FROM python:3.11

ENV PATH="/root/.local/bin:$PATH" 

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /awesome

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install


ENTRYPOINT [ "/bin/bash" ]