FROM python:3.12.1

LABEL MAINTAINER="Bekhruz yoshlikmedia@gmail.com"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python -u app.py