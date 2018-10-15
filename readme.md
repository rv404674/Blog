This is a web base blog application that has been created using Django (python) and sqlite3 as the db. It has many features including sharing post by email, comment system, pagination, searching using solr and haystack.

Requirements-
1. pip
2. virtualenv
3. django
4. Solr and Haystack

To run the project, do the following
1. source my_env/bin/activate
2. cd in mysite
3. "python3 manage.py createsuperuser"
(create a admin user with name and paswd)
4. "python3 manage.py runserver"
5. go to "localhost:8000/admin/" and create some users and posts.
6. go to "localhost:8000/blog/" to see all the features
