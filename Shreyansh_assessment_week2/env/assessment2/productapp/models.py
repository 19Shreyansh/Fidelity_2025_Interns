from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField(max_length=100)
    dop = models.DateField()

    def __str__(self):
        return self.name
