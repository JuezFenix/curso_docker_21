FROM python:3.8-slim

WORKDIR /app
ADD ./api/ /app

RUN apt update
RUN apt install vim -y procps -y 
RUN pip3 install -r requirements.txt

ENV MI_NOMBRE=RAMON

EXPOSE 8080

LABEL "author_name"="Ramón Molina"
LABEL "author_mail"="armolinamilla@gmail.com"

CMD ["python3", "app.py"]