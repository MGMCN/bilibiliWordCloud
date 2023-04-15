FROM ubuntu:20.04

LABEL maintainer="GAO SHAN"

ENV media_id="1586"

COPY . /proj

WORKDIR /proj/bilibili

RUN apt-get update && \
    apt-get install python3 python3-pip -y

CMD bash run.sh $media_id