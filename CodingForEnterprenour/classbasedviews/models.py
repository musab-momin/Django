from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class author(models.Model):
    name        = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title           = models.CharField(max_length=255)
    description     = models.TextField(null=True, blank=True)
    author          = models.ForeignKey(author, on_delete=models.CASCADE, blank=True, null=True)
    slug            = models.SlugField()
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return f"/classbasedviews/detailview/{self.slug}"
    
    

def book_model_pre_save_reciever(sender, instance, *args, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)


pre_save.connect(book_model_pre_save_reciever, sender=Book)
