# django-blog
A simple blog created with Django.

Installation
================

Make virtualenv
===============

On Linux::

   $ python -m venv env
   $ source env/bin/activate

On Windows::

   > python -m venv env
   > env/Scripts/activate

::

   (env)$ pip install -r requirements.txt

migrate
=======

::

   (env)$ cd DjangoBlog/
   (env)$ python manage.py migrate

Make admin user
===============

::

   (env)$ python manage.py createsuperuser

runserver
=========

::

   (env)$ python manage.py runserver
