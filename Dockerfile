FROM python:3
RUN mkdir /app
COPY . /app
CMD ["python3","/app/app.py"]