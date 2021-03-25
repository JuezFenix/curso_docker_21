FROM linuxserver/plex

ENV PUID=100
ENV PUID=1000
ENV PGID=1000
ENV VERSION=docker

VOLUME [ "/path/to/library:/config" ] 
VOLUME [ "/path/to/tvseries:/tv" ] 
VOLUME [ "/path/to/movies:/movies" ]

RUN apt update \
    && apt install net-tools \
    && apt install curl 