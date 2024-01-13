FROM ubuntu:xenial

RUN apt-get update && \
    apt-get install -y python3.6 python3.6-dev python3-pip && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1 && \
    update-alternatives --set python3 /usr/bin/python3.6 && \
    rm -f /usr/bin/python && ln -s /usr/bin/python3.6 /usr/bin/python

WORKDIR /app
COPY requirements.txt .
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.6 /usr/bin/python
RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.6 /usr/bin/python3

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn==19.9.0

ADD ./apps /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

RUN mkdir -p /app/backend/server/static