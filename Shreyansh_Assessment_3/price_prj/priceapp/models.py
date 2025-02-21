from django.db import models

# Create your models here.
class Price(models.Model):
    itemid = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)