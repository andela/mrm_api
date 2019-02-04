FROM python:3.6-slim

RUN apt-get update -u && apt-get install -y \
        supervisor \
        netcat \
        libglib2.0-0 \
        libxrender1 \
        libsm6 \
        libxext6 \
        libfontconfig1 \
        wget

RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && \
        tar xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

RUN chown root:root wkhtmltox/bin/wkhtmltopdf && \
        chmod a+x wkhtmltox/bin/wkhtmltopdf && \
        cp wkhtmltox/bin/wkhtmltopdf /usr/local/bin/


RUN chown root:root wkhtmltox/bin/wkhtmltoimage && \
        chmod a+x wkhtmltox/bin/wkhtmltoimage && \
        cp wkhtmltox/bin/wkhtmltoimage /usr/local/bin/

WORKDIR /app

COPY mrm_api.conf /etc/supervisor/conf.d/mrm_api.conf
COPY requirements.txt /app

RUN pip install -r requirements.txt && \
        pip install gunicorn && \
        pip install gevent
