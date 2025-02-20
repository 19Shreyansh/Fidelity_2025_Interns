from django.db import models

# Create your models here.
class Cars(models.Model):
    rank= models.IntegerField()
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
