# syntax=docker/dockerfile:1

FROM --platform=linux/amd64 python:3.10-slim-buster

RUN pip3 install --upgrade pip

WORKDIR /var/www/flask

COPY ./app /var/www/flask/app
COPY ./requirements.txt /var/www/flask/requirements.txt
COPY ./mental_unload.py /var/www/flask/mental_unload.py
COPY ./config.py /var/www/flask/config.py
COPY ./.env /var/www/flask/.env

ENV FLASK_ENV=development
ENV FLASK_APP=mental_unload

RUN pip3 install -r requirements.txt
# RUN flask db migrate

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]