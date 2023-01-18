FROM --platform=${BUILDPLATFORM} python:3.11 AS build

RUN apt-get update
RUN apt-get install -y libffi-dev libnacl-dev python3-dev
RUN python3 -m pip install -U pip

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt


FROM gcr.io/distroless/python3

ENV PYTHONPATH=/opt/python-app/lib

WORKDIR /awesome

COPY --from=build /usr/local/lib/*/site-packages /opt/python-app/lib
COPY src /awesome

CMD ["main.py"]