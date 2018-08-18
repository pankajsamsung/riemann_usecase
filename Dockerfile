FROM python:3.6

ADD . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT python3 program.py
