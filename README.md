# Sweet Mail

Sweet Mail is a mailing list manager that will let users start
mailing lists, sign up for mailing lists, and then message people. Subscribers will have to
confirm their subscription to a mailing list and be able to unsubscribe. This will help us to
ensure that Sweet Mail isn't used to serve spam to users. Sweet Mail provide also rest api endpoints
for mobile devices

# Tooling

* Django 2+
* Celery for asynchronous stuff
* Django rest framework
* Docker : postgres, redis
  
# How to run

* clone repo
* run

```bash

$ docker-compose up --build

```