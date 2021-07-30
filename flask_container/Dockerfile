FROM node:16-slim

EXPOSE 5000

WORKDIR /app

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip
RUN pip3 install --upgrade pip
COPY requirements.txt /app
RUN pip3 install  -r requirements.txt --upgrade pip

RUN npm install less -g

COPY . /app

CMD [ "uwsgi", "/app/app.ini" ]