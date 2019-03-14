FROM {{IMAGE}}

WORKDIR /app

COPY docker/prod/mrm_api.conf /etc/supervisor/conf.d/mrm_api.conf
COPY . /app

RUN pip install -r requirements.txt && \
        pip install gunicorn && \
        pip install gevent
