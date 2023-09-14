# Python-Django-API-DRF

Create a empty folder called 'booklist'
cd booklist
pipenv install django
pipenv shell
django-admin startproject BookList .
python manage.py startapp BookListAPI
pipenv install djangorestframework
open the settings.py in folder 'BookList', add 'rest_framework', 'BookListAPI' into the installed_apps
add code in view.py
create a file url.py inside BookListAPI folder and add code
update code in url.py inside BookList folder
python manage.py migrate
python manage.py runserver
if you change some file, you can run python manage.py makemigrations, then run python manage.py migrate


![Screenshot 2023-09-14 at 5 10 52 PM](https://github.com/bingtian730/Python-Django-API-DRF/assets/37897107/4f346696-960a-4d34-8da9-e5531ea5379a)
![Screenshot 2023-09-14 at 5 11 04 PM](https://github.com/bingtian730/Python-Django-API-DRF/assets/37897107/22174d4b-0dfa-4586-8865-73ff17e2d00a)
