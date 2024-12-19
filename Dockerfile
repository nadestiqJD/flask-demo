FROM ubuntu:latest
LABEL authors="macius"

RUN apt update && apt install -y python3.12 python3-pip python3-venv

RUN mkdir /opt/app && python3 -m venv /opt/app/venv

WORKDIR /opt/app

COPY requirements.txt ./requirements.txt

RUN venv/bin/pip install -r requirements.txt

COPY . .

ENV PORT=5000

EXPOSE 5000

CMD ["venv/bin/python", "app.py"]