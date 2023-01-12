FROM python:3.11

RUN apt-get update && \
    apt-get install -y libffi-dev libnacl-dev python3-dev && \
    python3 -m pip install -U pip

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

WORKDIR /awesome

ENTRYPOINT [ "/bin/bash" ]