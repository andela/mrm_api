FROM python:3.6

WORKDIR /app

RUN apt-get update -u && apt-get install -y \
        supervisor \
        netcat

RUN supervisord

COPY mrm_api.conf /etc/supervisor/conf.d/mrm_api.conf
COPY requirements.txt /app

RUN pip install -r requirements.txt && \
        pip install gunicorn && \
        pip install gevent 
