# Django Sample Project 

A sample project which takes email instead of username for login.

# Quick Deployment (Ubuntu)

* Open terminal

* Update Software Repositories

`sudo apt-get update`

* In home directory clone django-email-login

`sudo su`

`apt install git`

`git clone https://github.com/kamran890/django-email-login.git`

* Go to django-email-login directory

`cd django-email-login`

* Copy .env.example to new .env file

`cp .env.example .env`

* Open .env file and add env variables.

```
DEBUG=TRUE
SECRET_KEY=SECRET_KEY
```

* Run shell script

`./docker-deploy.sh`
