README
==================

Getting Started
---------------

- Crear virtualenv: virtualenv app

- Activar virtualenv: source app/bin/activate  

- cd <directorial atual>

- $VENV/bin/pip install -e .

- Reemplazar la cadena de conexion en el archivo development.ini: postgresql://<usuario>:<password>@<host>:<pass>/<dbname>

- initialize_kenwin_db development.ini

- pserve development.ini --reload

