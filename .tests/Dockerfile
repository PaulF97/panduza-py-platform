FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y mosquitto git

RUN apt-get install -y python3 python3-pip
RUN pip install git+https://github.com/behave/behave
RUN pip install PyHamcrest
RUN pip install coverage
RUN pip install loguru
RUN pip install paho-mqtt

RUN mkdir -p /etc/panduza
RUN touch /etc/panduza/tree.json

ENV PYTHONPATH="/work/panduza-py-platform:/work/panduza-py"

RUN mkdir /work

# RUN mosquitto -d

WORKDIR /work
