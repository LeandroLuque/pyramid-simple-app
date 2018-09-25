README
==================

Getting Started
---------------

- Crear virtualenv: virtualenv .app

- Activar virtualenv: source .app/bin/activate  

- cd *carpeta del proyecto*

- pip install -e .

- Reemplazar la cadena de conexion *sqlalchemy.url* en el archivo development.ini: postgresql://usuario:password@host:pass/dbname

- initialize_kenwin_db development.ini

- pserve development.ini --reload


Screenshots
---------------

- [Home screen](images/1.png)
- [Login screen](images/2.png)
- [Logged user](images/3.png)

Project created with **pcreate -s alchemy** 