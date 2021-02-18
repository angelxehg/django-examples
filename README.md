# Django Examples

Ejemplos hechos con Django 3.1

## Instalación

Para instalar de manera local ejecute los siguientes comandos:

- Instalar dependencias: `sudo apt install python3 python3-pip python3-virtualenv`
- Crear un entorno virtual: `virtualenv .venv/`
- Activar entorno virtual: `source .venv/bin/activate`
- Instalar paquetes: `pip3 install -r config/requirements.txt`

Se requiere configurar la base de datos y un super usuario antes de iniciar el servidor:

- Migrar estructura base de datos: `./manage.py migrate` (se usará SQLite por defecto)
- Crear un super usuario: `./manage.py createsuperuser`
- Iniciar servidor local: `./manage.py runserver` (panel de control en [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin))
- Ejecutar pruebas unitarias: `./manage.py test`

## Despliegue en Heroku

Para instalar en Heroku ejecute los siguientes comandos:

- Crear aplicación en Heroku: `heroku create`
- Generar clave secreta: `./keygen.py`
- Configurar clave secreta: `heroku config:set SECRET_KEY="[SECRET_KEY]"`
  - Ejemplo de clave secreta: `heroku config:set HOST="BrMyuVBC1wod4VzPNC93A24ypFzHhG0VVLF8VYe6OW0"`
- Configurar Heroku host: `heroku config:set HOST="[Heroku URL]"`
  - Ejemplo de Host: `heroku config:set HOST="https://salty-beyond-27706.herokuapp.com/"`
- Configurar production settings: `heroku config:set DJANGO_SETTINGS_MODULE=django_examples.production`
- Hacer Git Push a Heroku: `git push heroku main`
- Crear un super usuario: `heroku run python manage.py createsuperuser`

La operación de configuración y migración de la base de datos se ejecuta automáticamente en Heroku en cada Push

## Recursos

Use los siguientes materiales de apoyo para desarrollar con Django

- [Documentación Django](https://docs.djangoproject.com/en/3.1/)
- [Extensión Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Extension Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Extensión Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
