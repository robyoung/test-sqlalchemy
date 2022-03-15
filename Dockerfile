FROM python:3.10

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  wget \
  curl \
  build-essential \
  libpq-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry==1.1.12 && \
  poetry config virtualenvs.create false && \
  poetry install

COPY . .

USER www-data

CMD ["bash"]
