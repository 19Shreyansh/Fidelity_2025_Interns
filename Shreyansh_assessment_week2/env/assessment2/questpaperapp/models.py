from django.db import models

# Create your models here.
class Question(models.Model):
    subject=models.CharField(max_length=100)
    qno=models.IntegerField(primary_key=True)
    quest=models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject
