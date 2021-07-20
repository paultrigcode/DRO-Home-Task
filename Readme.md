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

The API uses JWT for Authentication, so you need to use the superuser credentials you created above to authenticate the api on postman or insomnia. Then copy the access_token to your postman/insomnia environment to make subsequent authenticated request to the create_cycles and cycle_event end_point.

The screenshot below shows The endpoints and body required and expected JSON response
1) Authentication Endpoint
<img width="1009" alt="Screenshot 2021-07-20 at 22 05 23" src="https://user-images.githubusercontent.com/27996978/126397214-9f7a3ed4-602f-4bac-9aee-199e420badfc.png">

2) Create Cycle Endpoint
<img width="1009" alt="Screenshot 2021-07-20 at 22 25 46" src="https://user-images.githubusercontent.com/27996978/126397556-bee390dc-fe18-4ab6-9e17-2d3332074b1f.png">

3) Get Cycle Event For a spevific date in date range
<img width="1042" alt="Screenshot 2021-07-20 at 22 27 41" src="https://user-images.githubusercontent.com/27996978/126397713-ec6e78cf-3cbf-4d2b-a119-154a3c2e90ad.png">

For each request you make you need to pass the Bearer auth token in the header of each request as shown in the screenshot below
<img width="1042" alt="Screenshot 2021-07-20 at 22 29 42" src="https://user-images.githubusercontent.com/27996978/126397942-803da8b9-f2e3-4b76-8231-a83ece3ca5db.png">
Where ._auth_4 is the access_token gotten from the authentication endpoint and passed to your insomnia environment

