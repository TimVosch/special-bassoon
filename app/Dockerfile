FROM python:3.6

RUN pip3 install pipenv

ARG uid=1000
ARG gid=1000
RUN groupadd -g $gid nens && useradd -lm -u $uid -g $gid nens

VOLUME [ "/opt/code" ]

WORKDIR /opt/code
USER nens