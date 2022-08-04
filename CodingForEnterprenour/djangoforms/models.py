from platform import release
from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.
class Car(models.Model):
    name            = models.CharField(max_length=100)
    company_name    = models.CharField(max_length=100)
    price           = models.IntegerField()
    release_date    = models.DateField()
    created_at      = models.DateTimeField(default=timezone.now)
    
    
    class Meta:
        verbose_name_plural = 'Cars'

    
    def __str__(self):
        return self.name