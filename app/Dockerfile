FROM python:3.8.10-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN python3 -m venv .
RUN python3 -m pip install pip==21.1.1
RUN python3 -m pip install setuptools==56.2.0
RUN python3 -m pip install psycopg2-binary
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 8082
#CMD ["gunicorn", "--bind", ":8082", "server:app"]