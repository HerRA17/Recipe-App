# Recipe App
## Overview
This web application is built by python using 'Django' framework. It's a fully-fledged app with an admin panel to perform CRUD operations on the database and letting users sign up, update their profile, and create their own recipes. 

## Key Features:
1. **Recipe Management**: Create, edit, and organize your favorite recipes. Include detailed information such as ingredients, instructions, and estimated cooking time.

2. **Search and Filters**: Easily search for recipes based on keywords, ingredients, or categories. Apply filters to narrow down your recipe options and find the perfect dish. 

3. **Data Visualization**: Visualize recipe data through interactive charts, allowing users to gain insights into cooking times, ingredient usage, and more.

## Getting Started:
To begin using the Recipe-App Management, follow these steps:

+ **Prerequisites**:
    - Python 3.11.5
    - Django 4.2.6

+ **Installation**:
    1. Clone the project repository from GitHub to your local machine.
       ```
       git clone https://github.com/torbalansky/recipe-app.git
       cd recipe-app
       ```
    2. Install all required Python packages.
       ```
       pip install -r requirements.txt
       ```
    3. Configure the database settings in the project's settings file.
    4. Apply necessary database migrations.
       ```
       python manage.py migrate
       ```
    5. Launch the development server.
       ```
       python manage.py runserver
       ```

+ **Important Remarks**:
    Sensitive data, such as the secret key, DB details, and debugging information, were stored in a .env file. The key that was visible in previous steps is a dummy.

## Dependencies
* **Python** (3.11) - [Link to Python](https://www.python.org/)
* **Django** (4.2.6) - [Link to Django](https://www.djangoproject.com/)
* Other Python libraries (please review the requirements.txt file)
* **Databases alternatives**:
    * The default SQLite
    * To host in Pythonanywhere, it is suggested PostgreSQL for example.

+ **Database Migration Steps for PostgreSQL usage**:
    1. Create a database either in the psql shell or AdminPg4.
    2. Install package psycopg2.
    3. Proceed with `py manage.py dumpdata > name_file` (ex. data.json) (can be python, depending on the OS you are using).
    4. Check encoding, it needs to be changed from utf-16 to utf-8.
    5. Now you should change your `settings.py` (Database portion).
       Example: 
       From what you have to something similar:
       ```python
       DATABASES = {
           'default' : {
               'ENGINE': 'django.db.backend.sqlite3',
               'NAME': BASE_DIR / 'db.sqlite3'
           }
       }
       ```
       To:
       ```python
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.postgresql_psycopg2',
               'NAME': config('DB_NAME'),
               'USER': config('DB_USER'),
               'PASSWORD': config('DB_PASSWORD'),
               'HOST': config('DB_HOST'),
               'PORT': config('DB_PORT')
           } 
       }
       ```
    6. Sync the data:
       ```
       py manage.py migrate --run-syncdb
       ```
    7. After synchronizing the data, delete the default data:
       ```
       py manage.py shell
       >>> from django.contrib.contenttypes.models import ContentType
       >>> ContentType.objects.all().delete()
       ```
    8. Ship the data to PostgreSQL:
       ```
       py manage.py loaddata data.json
       ```

* **Frontend Frameworks**:
    - Bootstrap: [Link to Bootstrap](https://getbootstrap.com/)
    - jQuery: [Link to jQuery](https://jquery.com/)
