from django.db import models
from django.utils import timezone
from django.conf import settings
from learning_models.validations import validate_email, validate_title
from django.db.models.signals import post_save



# Create your models here.
# Create model for blog post

# PUBLISH_CHOICES = (
#     ('DF', 'Draft'),
#     ('PB', 'Publish'),
#     ('PR', 'Private')
# )

# class Post(models.Model):
#     title = models.CharField(max_length=50, validators=[validate_title])
#     content = models.TextField(blank=True)
#     status = models.CharField(max_length=2,choices=PUBLISH_CHOICES, default="DF")
#     view_count = models.IntegerField(default=0)
#     publish_date = models.DateField(default=timezone.now)
#     is_active = models.BooleanField(default=True, editable=False)
#     author_email = models.CharField(
#                         max_length=150, 
#                         validators=[validate_email], 
#                         blank=True, 
#                         unique=True,
#                         error_messages={
#                             'unique': 'This email is already registered. Try different one.'
#                         }, help_text='There is account with this email. either login or try different email')

#     #we can override save method but in some cases it is usefull not all the type
#     #def save(self, *args, **kargs):
#         #super(Post, self).save(*args, **kargs)


#     def __str__(self):
#         return self.title


# #user model

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     status = models.CharField(max_length=100, blank=True)


#     def __str__(self):
#         return self.user.username
    

# #using a signal to create profile automatically when the user object gets created. It is possible bcoz of signals

# #we have to write a function for signal and assoiate this function with user object when user obj is created call this function
# #to create profile for that user this function takes 3 parameters sender(who send the signal), instance(user obj), 
# # created(is user obj created it's a boolean value)
# def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             Profile.objects.create(user=instance)
#         except Exception as ex:
#             print(ex)


# post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)


#django aggregation starts
# class City(models.Model):
#     name = models.CharField(max_length=100)
#     population = models.IntegerField(default=0)


#     def __str__(self):
#         return  self.name



# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

#     def __str__(self):
#         return  self.name


# class Publisher(models.Model):
#     name = models.CharField(max_length=300)
    
#     def __str__(self):
#         return  self.name


# class Book(models.Model):
#     name = models.CharField(max_length=300)
#     pages = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     rating = models.FloatField()
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     pubdate = models.DateField()

#     def __str__(self):
#         return  self.name


# class Store(models.Model):
    # name = models.CharField(max_length=300)
    # books = models.ManyToManyField(Book)

    # def __str__(self):
    #     return  self.name


#for prefetch_related and selecte_related

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=60)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    