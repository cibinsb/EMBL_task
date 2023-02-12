FROM python:3.11.2
ADD . /app
WORKDIR /app
COPY config/gunicorn_config.py /app
RUN pip install -r config/requirements.txt
CMD ["gunicorn","app:api","-b","0.0.0.0:8080","-c","config/gunicorn_config.py"]
