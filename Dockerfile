FROM python:3.11 AS build

RUN apt-get update
RUN apt-get install -y libffi-dev libnacl-dev python3-dev
RUN python3 -m pip install -U pip

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt
