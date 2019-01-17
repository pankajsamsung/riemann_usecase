FROM python:3.5.2

ADD . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT python3 program.py
