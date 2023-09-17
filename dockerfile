FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && install awscli -y

RUN pip install -r requirements.text

CMD ["python 3","app.py"]