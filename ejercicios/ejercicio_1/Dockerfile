FROM ubuntu:20.04

#Install apache2
RUN apt-get update &&\ 
    apt-get install -y apache2 &&\ 
    apt-get clean &&\ 
    rm -rf /var/lib/apt/lists/*

#Define values for uses environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

#publish a PORT
EXPOSE 80

#start the server
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
