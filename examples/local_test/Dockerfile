FROM ubuntu:22.04

RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip
RUN pip install loguru
RUN pip install paho-mqtt
RUN pip install python-magic
RUN pip install behave-html-formatter

RUN mkdir /etc/panduza
ENV PYTHONPATH="/workdir/panduza-py-platform"

WORKDIR /workdir
