# syntax=docker/dockerfile:1

FROM python:3.10.2-slim-bullseye

WORKDIR ./

RUN pip3 install paho-mqtt

COPY subscriber.py .

CMD [ "python3", "subscriber.py"]