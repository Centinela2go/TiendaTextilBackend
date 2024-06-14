## Creación de virtual enviroment
```bash
python -m venv .env
```

- Activar virtual enviroment
```bash
source .env/Scripts/activate
```

## Instalar los paquetes requeridos
```bash
pip install -r requirements.txt
```

## Crear proyecto
Este comando crea una aplicacion django en la misma carpeta
```bash
django-admin startproject config .
```

## Crear una aplicacion
```bash
django-admin startapp name_app
```

## Registrar migraciones
```bash
python manage.py makemigrations
```

## Confimar migraciones
```bash
python manage.py migrate
```

## Correr el proyecto
```
python manage.py runserver
```