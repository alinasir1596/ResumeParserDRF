web: gunicorn core.wsgi
python manage.py collectstatic
python manage.py makemigratations
python manage.py migrate
python manage.py runserver