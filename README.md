# ToDoList
## Autor
**Carlos Gonzalez**
La siguiente es una prueba para un puesto de trabajo con Ensolvers.

Consiste en una aplicación web sencilla, la cual permite: 

## Descripcion
* Registrar usuarios
* Loguear usuarios
* Crear carpetas asociadas a cada usuario
* Crear dentro de cada carpeta, actividades asociadas a cada una

## Tecnologías
_En el proyecto se encuentra un archivo requirements.txt con todo lo necesario para ejecutar el mismo, sin embargo,
se describen a continuación:_

- Python 3.6
- PostgreSQL
- asgiref 3.3.1
- dj-database-url 0.5.0
- Django 3.1.7
- django-widget-tweaks 1.4.8
- gunicorn 20.1.0
- psycopg2 2.8.6
- pytz 2021.1
- sqlparse 0.4.1

En pocas palabras, se utilizó Django como framework para el desarrollo de la aplicación web y postgreSQL en su version 13

La base de datos no se debe instalar ni configurar localmente, pues la misma ya se encuentra en un servidor de AWS

## Para correr el proyecto

_Se incluye un archivo run.sh probando únicamente en Linux Ubuntu 20.04, dicho archivo se encarga de:_

1) Instalar python 3
2) Instalar python pip
3) Instalar python venv (para crear entornos virtuales)
4) Instala las dependencias del archivo requirements.txt en el entorno virtual
5) Ejecuta el proyecto

Para ejecutar el archivo, desde la terminal se debe ingresar a la carpeta del proyecto y ejecutar "./run.sh".
De arrojar algun error antes de iniciarse, es importante dar permisos de ejecución a dicho archivo.

Sin embargo, en caso de que algo falle, para poder ejecutar el proyecto:

1) Se debe instalar python 3 (preferiblemente 3.6 en adelante)
2) Instalar pip con el comando sudo apt install python3-pip
3) Instalar python venv mediante el comando "sudo apt install python3-venv"
3) Ahora se crea un entorno virtual, "python3 -m venv entorno"
4) Activamos el entorno virtual: "source entorno/bin/activate"
5) Con el entorno virtual activo, ejecutamos "pip install -r requirements.txt"
6) Finalmente, ejecutar con el entorno virtual activo "python manage.py runserver"

## Acceder al proyecto online

_El proyecto fue subido también a un servidor de Heroku en el que se puede probar sin necesidad de realizar insalaciones_

El mismo se puede encontrar en el siguiente enlace: 

https://powerful-thicket-43913.herokuapp.com/

* Usuario por ya creado: carlox97
* Contraseña: mynameiscarlos

Con dicho usuario se podran visualizar algunos ejemplos ya creados previamente, sin embargo, también es posible crear un usuario nuevo a través
de la funcionalidad de Sign Up

## Importante a tener en cuenta

Únicamente en el servidor (con debug= False) funciona un feature que básicamente permite redirigir las peticiones a urls que no existen, por ejemplo, si se intenta acceder a la url /ToDoList/newList (la cual no existe) en el servidor esta solicitud será redirigida a una url por defecto.

Sin embargo, si se realiza lo mismo con la versión local que se obtiene al clonar este repositorio (debug = True) dicha funcionalidad, a pesar de estar también implementada, no se encuentra activa por la manera en que funciona Django. En este caso, se mostrará un mensaje de error de Django indicando que no se encontró la URL.

Por favor les agradezco comunicarse conmigo ante cualquier duda o inquietud que pudiera surgir
