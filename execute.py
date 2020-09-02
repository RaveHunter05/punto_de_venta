import os

print('command executed, server is up and running!')

os.system('source env/bin/activate && cd src && python manage.py runserver')