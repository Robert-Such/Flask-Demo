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

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

CMD [ "uwsgi", "/app/app.ini" ]