# curso_docker_21
Documentacion y ejercicios del curso Docker 21

## Ejercicios

### Ejercicio 1
Creación de una imagen basada en Ubuntu 20.04, instalarle Apache2 limpiar el execeso de información y exponer el puerto 80.

Construcción de la imagen

`docker build -t armm_ejercicio1 ejercicios/ejercicio_1/`

Creación de contenedores

`docker run -p 8081:80 armm_ubuntu`

## Ejercicio 2
Docker compose que descarga y generar un contendor Apache2 y otro contenedor MySql y activa la conexión entre ellos.

Creación de contenedores

`docker-compose up`

## Ejercicio 3
Diseño de una imagen basada en ubuntu, que copia ficheros python que ejecutan un servidor Flask y exponen una API con la uri /hola para saludar con el nombre indicado en la variable de entorno MI_NOMBRE.

Construcción de la imagen

`docker build -t armm_ejercicio3 ejercicios/ejercicio_3`

Cración de contenedores

`docker run -p 8080:8080 armm_ejercicio3`

Url para probar la API

`http:\\localhost:8080/hola`
