FROM alpine:3.17.3

LABEL maintainer="GAO SHAN"

ENV media_id="1586"

COPY . /proj

WORKDIR /proj

RUN apk --update-cache add \
    python3 \
    python3-dev \
    py3-pip \
    gcc \
    build-base \
    bash \
    libffi-dev && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

WORKDIR /proj/bilibili

CMD bash run.sh $media_id