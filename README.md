# django-blog
A simple blog created with Django.


# Installation


### Make virtualenv

On Linux:

   >  python -m venv env
   >  source env/bin/activate

On Windows:

   > python -m venv env
   > env/Scripts/activate

Install dependencies:

   > pip install -r requirements.txt

### Migrate



   > cd DjangoBlog/
   > python manage.py migrate

### Make admin user

   > python manage.py createsuperuser

### Run server
   > python manage.py runserver
