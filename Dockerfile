FROM python:3.13.0a4

LABEL MAINTAINER="Bekhruz yoshlikmedia@gmail.com"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python -u app.py