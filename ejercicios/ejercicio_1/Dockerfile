FROM ubuntu

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && apt-get install -y apache2 \
    && apt-get clean

EXPOSE 80
CMD apachectl -D FOREGROUND