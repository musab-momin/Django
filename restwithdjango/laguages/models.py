from django.db import models


# Create your models here.
class LanguageInventor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Language(models.Model):
    name = models.CharField(max_length=50)
    pradigm = models.CharField(max_length=50)
    inventor = models.ForeignKey(LanguageInventor, models.CASCADE)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
    
