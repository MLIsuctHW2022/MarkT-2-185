FROM python:3.9.16

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
