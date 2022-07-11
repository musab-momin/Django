from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomAccountManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError('User must need a email')
        
        if not username:
            raise ValueError('User must need a username') 

        user = self.model(
            email= self.normalize_email(email), 
            username = username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        print(f'''
            This is Email: 
            {email}
            This is the password 
            {password}
        ''')

        user = self.model(
            email= self.normalize_email(email), 
            username = username)

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




#path to save profile image
def get_profile_image_filepath(self, filename):
    return f"profile_images/{self.pk}/profile_image.jpg"

#get default image
def get_default_image_filepath():
    return "assets/default.jpg"



# Create your models here.
class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email', max_length=100, unique=True)
    username        = models.CharField(verbose_name='username', max_length=150, unique=True)
    profile_image   = models.ImageField(max_length=255,upload_to = get_profile_image_filepath, default=get_default_image_filepath, null=True, blank = True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    hide_email      = models.BooleanField(default=True)


    objects         = CustomAccountManager()      #setting up the custom account manager


    USERNAME_FIELD  = 'email'                      #now email is required for login email is username
    REQUIRED_FIELDS = ['username']                 #if we want to make username unique


    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image[str(self.profile_image).index(f"profile_images/{self.pk}/"):])

    def has_perm(self, perm, obj=None):            #we have to overide this metod to set permission for new user
        return self.is_admin
    
    def has_module_perms(self, app_label):         #this a model permission for new user
        return True
    