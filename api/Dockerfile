FROM python:alpine

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir