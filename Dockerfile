FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y vim

RUN pip install --no-cache-dir -r requirements.txt

COPY ./.docker/entrypoint.sh /

COPY . .

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

USER 1000

EXPOSE 7676

ENTRYPOINT ["/entrypoint.sh"]
