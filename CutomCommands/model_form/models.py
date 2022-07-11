from django.db import models


# Create your models here.
class Computer(models.Model):
    brand   = models.CharField(max_length=100)
    name    = models.CharField(max_length=100)
    price   = models.CharField(max_length=30)


    def __str__(self):
        return self.name


