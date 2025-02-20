from django.db import models

# Create your models here.

class Profile(models.Model):
    eID = models.CharField(max_length=50,primary_key=True)
    emp_name = models.CharField(max_length=100,blank=True)
    emp_email = models.EmailField(max_length=50)
    emp_passw = models.CharField(max_length=100,null=False)  
    emp_doj = models.DateField()