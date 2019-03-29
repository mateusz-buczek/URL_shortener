# URL_shortener
web app shortening long urls

# General info
The visual aspect is devoloped to the level that makes it usable. However it's supposed to work, not to be miss universe ;) Also i'm not proficient front-end dev. 

# Features 
Your can shorten your long URL in two ways: 
- provide custom name in "Shortened: " field 
- get random name by leaving "Shortened: " blank 

If you try to use name that is already taken id DB, page will reload with provided input (i'm working on proper warning message)

# Technologies 
* Python 3.7.2
* Django 2.1.7 
* SQLite (Django's default DB)
* HTML
* CSS 
* Bootstrap 3.4.0 (bootstrapcdn.com) 

# Setup 
Copy this repository to your HDD or choose corresponding option in your IDE (PyCharm recommended). 
Install Django: 
```
$ pip install django 
```
Pycharm should create venv for you. If not, choose default Python based one when asked. 
If you're impatient type: 
```
$ cd mysite
```
and then (when in folder mysite): 
```
$ py manage.py runserver 
```
which will probably give you only django welcome site at 127.0.0.1:8000 because of unapplied SQL migrations (database in .gitignore). Hit ctrl+C or break.
Go ahead and do the following: 
```
$ py manage.py migrate
$ py manage.py makemigrations shortener
$ py manage.py sqlmigrate shortener 0001 
```
and again: 
```
$ py manage.py migrate 
```

From now on 
```
$ py manage.py runserver  
```
should run main site and shortener is ready to use. Go ahead try it out and populate DB. 
IMPORTANT! don't change the port, it needs to run on http://127.0.0.1:8000/ address 


Feel free to send feedback :) 

# Sources/Inspirations 
This work is based on Django documentation and free bootstrap template from www.w3schools.com 
