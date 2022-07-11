from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils.timesince import timesince
from blog.validators import email_validator



PUBLISH_CHOICE = [
    ('df', 'Draft'),
    ('pb', 'Public'),
    ('pr', 'Private')
]


#by default django give us a model manager for each model but we can overide the methods of model manager
#just create a class and extend it with model.Manager class and override any method you want 
#here I overided the all method I just want to return only the post whos active is True
class PostManager(models.Manager):

    #overinding all method
    def all(self, *args, **kwargs):
        return super(Post, self).all(*args, **kwargs).filter(active=True)


# Create your models here.
class Post(models.Model):
    id              = models.AutoField(primary_key=True)
    active          = models.BooleanField(default=True)
    title           = models.CharField(max_length=200, verbose_name='Post Title')
    slug            = models.SlugField(null=True, blank=True, editable=True)   #editable is by default true which means during the form fillup we can edit that field if we make editable false than it will not appear on forms.
    content         = models.TextField(null=True, blank=True)
    choice          = models.CharField(max_length=100, choices=PUBLISH_CHOICE, default='df')
    views_count     = models.IntegerField(default=0)
    publish_date    = models.DateTimeField(default=timezone.now)
    author_email    = models.CharField(max_length=100, validators=[email_validator], null=True)     #I am using a email validator we can pass multiple validation functions for a single field


    objects         = PostManager       #connecting our custom manager with our model

    class Meta:
        verbose_name_plural = 'Posts'

    
    def __str__(self):
        return self.title

    #We can declair instance methods as much as we want. Django also have some instance methods e.g: timesince 
    #timesince returns the time when the db record was created or in other words returns the age of record
    def get_age(self):
        if self.choice == 'df':
            return "Not posted yet"
        elif self.choice == 'pr':
            return 'private post'
        return f'{timesince(self.publish_date)} ago'

    #overiding save method this is not recomended to do until you need this
    #here we want to create a slug for every blog post so we override the save method and on each save we are adding slug
    #this is a nice case were you want to overide the save method.
    # def save(self, *args, **kwargs):
    #     if not self.slug and self.title:
    #         self.slug = slugify(self.title)
    #         super(Post, self).save(*args, **kwargs)



#remember I said it is not consider good practice to overide the save method. There for we have singnals this are like
#normal signals which are get called before creating model and after creating a model we can use pre_save signal to add
#slugs to over instance or database entry
def post_model_pre_save_reciever(sender, instance, *args, **kwargs):
    print('Slug is added by pre save reciever')
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(post_model_pre_save_reciever, sender=Post)