from django.db import models

# Create your models here.
class Location(models.Model):
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pincode=models.IntegerField(null=True)