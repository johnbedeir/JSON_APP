FROM python:3

MAINTAINER "john.bedeir@gmail.com"

COPY ./APP /home

CMD ["python3","/app/APP/app.py"]