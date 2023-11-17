# Recipe App
## Overview
This web application is built by python using 'Django' framework. It's fully fledged app with admin panel to perform CRUD operationas on the database and letting users sign up, update their profile and create their own recipes. 
## Key Features:
1. Recipe Management: Create, edit, and organize your favorite recipes. Include detailed information such as ingredients, instructions, and estimated cooking time.

2. Search and Filters: Easily search for recipes based on keywords, ingredients, or categories. Apply filters to narrow down your recipe options and find the perfect dish. 
 
3. Data Visualization: Visualize recipe data through interactive charts, allowing users to gain insights into cooking times, ingredient usage, and more.

## Getting Started:
To begin usign the Recipe-App Management, follow the following steps:
+ Make sure you have installed the following software:
    * Python 3.11.5
    * Django 4.2.6
+ Installation:
    1. Clone the project repository from github to your local machine.
       ```git clone https://github.com/torbalansky/recipe-app.git```
        ```cd recipe-app```
    2. Install all required Python packages.
       ```pip install -r requirements.txt```
    3. Configure the databases settings in the project's settings file.
    4. Apply necessary database migrations.
       ```python manage.py migrate```
    5. Launch the development server.
        ```python manage.py runserver```
+ Important remarks:
    Sensitive data, such as the secret key, DB details, and debugging information, were stored in a .env file. The key that was visible in previous steps is a dummy.

## Dependencies
* Python (3.11)
     <a href="https://www.python.org/">Link to Python</a>
* Django (4.2.6) 
    <a href="https://www.djangoproject.com/">Link to Django </a>
* Other Python libraries (please review the requirements.txt file)
* Databases
    * Initially with the default sqlite
    * To hosted in Pythonanywhere I migrated it to Postgredql
    + Steps:
        1. Create a database either in the psql shell or AdminPg4
        2. Install package psycopg2
        3. Proceed with py manage.py dumpdata > name_file(ex. data.json) (can be python, depending the OS you are using)
        4. Check enconding, it needs to be changed from utf-16 to utf-8
        5. Now you should change your settings.py (Database portion)
        ex- from what you have to something similar
        prev:
        DATABASES = {
            'default' : {
                'ENGINE': 'django.db.backend.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3'
            }
        }

        afterwards:
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST':config('DB_HOST'),
            'PORT':config('DB_PORT')
            } 
        }
        6. Now we need to sync the data:
        py manage.py migrate --run-syncdb
        7. After the syncronizing the data, we now should delete the default data:
        py manage.py shell
        >>> from django.contrib.contenttypes.models import ContentTypes
        >>> ContentType.objects.all().delete()
        8. Last, we need to shipp the data to Postgresql:
        py manage.py loaddata data.json (int he shell should we see rows and columns displaying the data)

* Frontend Frameworks:
    Bootstrap: <a href="https://getbootstrap.com/">Link to Bootstrap</a>
    jQuery <a href="https://jquery.com/">Link to jQuery</a>