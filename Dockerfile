FROM python:3.8

LABEL maintainer="GAO SHAN"

ENV media_id="1586"

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /proj

COPY . /proj

WORKDIR /proj/bilibili

CMD bash run.sh $media_id