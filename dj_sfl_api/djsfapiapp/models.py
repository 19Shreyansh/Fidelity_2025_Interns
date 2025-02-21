from django.db import models

class Trip(models.Model):
    trip_id = models.BigAutoField(primary_key=True)
    trip_cost = models.DecimalField(max_digits=10, decimal_places=2)
    trip_date = models.DateField()
    travellers = models.IntegerField()
    boardingpoint = models.TextField()
    destination = models.TextField()