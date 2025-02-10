#django = rapid web application development framewrok and easy management
#database connected to djanh=go onserver is called a model
#MVC is model view controller .
#model is database
#view is whatever we are seeing
#controller . it has an inbuild controller unlike spring boot. 
#django is MVT based
#t for template. it has ready made template which makes it easier 
#virtualization = create a virtual environment = can be used to isolate dependecy to avoid compatibility issue

#apache runs on a backend server which processes our request and gives a response
#python -m venv (project_name)
#python -m venv env
#env\Scripts\activate to activate a virtual environment
#pip list 
#pip install numpy 

#to send data to backend , use get or post
#for get data will be in search bytearray
#for post data will be in http body3 with csrf security


#create a folder
#python -m venv env
#env\Scripts\activate
#pip install django
#django-admin startproject projectname
#pyhton manage.py runserver / python manage.py startapp myapp
#create urls.py
#inslude inside in project url.py inside myapp.url
#path('myapp'/(include(myapp.urls)))
#myapp



#when we create model in app , add it in admin.py
#import the model and 
#orm is object relational mapping to map the classes in java or python striaght into tables
#TO BE DONE ONLY FIRST TIME python manage.py makemigrations to according to thid model orders is created . IT is for making changes into maodels like adding extra fields
#pythpn manage.py migrate creates the table into database according to model