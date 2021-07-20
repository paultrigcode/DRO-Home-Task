# DRO Women's health API

This project implements a REST API that helps estimate a woman’s period cycles within a specific timeframe. Additionally, it also implements another REST API to determine what period of her monthly cycle a lady is currently in.


## Installation
In order to run the code on your local machine , first you need to  create a virtualenv, next is to activate the virtualenv and install the libraries in the `requirements.txt` file. 

## How to run the app

First, clone the repository, go into the source code directory, create a virtualenv and install the required python libraries by running the following command:


```
cd DRO-Home-Task-master
virtualenv .
source bin/activate
pip install -r requirements.txt
```

```

```
python manage.py makemigrations
python manage.py migrate
```
Now run the command below to create superuser
```
python manage.py createsuperuser
```
After creating superuser, 
```
python manage.py runserver
```

```
```
make sure to run the above commands in the directory containg "manage.py" file


## Process diagram
 ![Flow Diagram](Process_flow.png)


## Usage
Import The Insomia APi collcetion and Check The Insomnia DOC to see the list of available endpoints and how to use them
 #  The following API endpoints have been defined and can be tested on postman or insomnia as follows
 1)POST : http://127.0.0.1:8000/api/token/ (Authentication)
 2) POST: http://127.0.0.1:8000/womens-health/api/create-cycles/
 3) GET : http://127.0.0.1:8000/womens-health/api/cycle_event/: param : date

 Import the insomnia Collection in repo on postman or insomnia to see the list of available endpoints together with their descriptions on how
 they are to be called and used. you can also see the list of avialable endpoint by going to

 [Link to Swagger DOC](http://127.0.0.1:8000redoc/)



```
```
```
## How to use the API

The API uses JWT for Authentication, so you need to use the superuser credentials you created above to authenticate the api on postman or insomnia. Then copy the access_token to you postman/insomnia environment to make subsequent authenticated request to the create_cycles and cycle_event end_point.


