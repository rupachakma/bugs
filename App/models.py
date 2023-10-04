from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField(max_length=20)
    quantity=models.CharField(max_length=100)
    price=models.IntegerField()

def __str__(self):
    return self.name
