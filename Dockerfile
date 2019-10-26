FROM python:3.6
ADD . /app
WORKDIR /app
COPY config/gunicorn_config.py /app
RUN pip install -r config/requirements.txt
