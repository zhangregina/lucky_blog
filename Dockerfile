FROM python:3.9
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

ADD . /app/

