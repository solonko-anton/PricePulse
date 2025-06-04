FROM python:3.12-slim

ENV PYTHONDONTBUFFERED=1
ENV PYTHONDONTWRITEBYTCODE=1

WORKDIR /code

RUN apt-get update && \
    apt-get install -y curl && \
    curl -Ls https://astral.sh/uv/install.sh | sh && \
    apt-get clean

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock /code/

RUN uv sync

COPY . .

CMD ["uv", "run", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]


