from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id=models.CharField(max_length=100)
    prod_name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField()

    def __str__(self):
        return f"{self.prod_name}"
