FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /api

ENV UV_COMPILE_BYTECODE 0
ENV UV_LINK_MODE=copy

ADD . /api
RUN uv venv --python 3.12.4
RUN uv sync

ENV PATH="/api/.venv/bin:$PATH"

ENTRYPOINT []

CMD ["make", "run-api"]

EXPOSE 8000
