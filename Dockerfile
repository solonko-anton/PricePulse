FROM python3.12:silm

ENV PYTHONDONTBUFFERED=1
ENV PYTHONDONTWRITEBYTCODE=1

WORKDIR /code

RUN apt-get update && \
    apt-get pip install uv 

COPY pyproject.toml /code/

RUN uv add pyproject.toml

COPY . .