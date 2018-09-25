README
==================

Getting Started
---------------

- Crear virtualenv: virtualenv app

- Activar virtualenv: source app/bin/activate  

- cd <directorial atual>

- pip install -e .

- Reemplazar la cadena de conexion *sqlalchemy.url* en el archivo development.ini: postgresql://<usuario>:<password>@<host>:<pass>/<dbname>

- initialize_kenwin_db development.ini

- pserve development.ini --reload

