from django.db import models
from django.conf import settings
from psycopg2 import Timestamp


# Create your models here.
class PublicChatRoom(models.Model):
    title       = models.CharField(max_length=200, unique=True, blank=False)
    users       = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text="Users who are active are connected to the chat")


    def __str__(self):
        return self.title


    #return true if user is added to the users list
    def connect_user(self, user):
        is_user_added = False
        if not user in self.users.all():
            self.users.add(user)
            self.save()
            is_user_added = True
        elif user in self.users.all():
            is_user_added = True
        return is_user_added
     
        
    #return true if user is removed to the users list
    def disconnect_user(self, user):
        is_user_removed = False
        if user in self.users.all():
            self.users.remove(user)
            self.save()
            is_user_removed = True
        elif not user in self.users.all():
            is_user_removed = False
        return is_user_removed
    
    
    @property
    def group_name(self):
        '''
        return the channels group name that sockets should subscribe to and get sent messages aas thhey are generated.
        '''
        return f'PublicCharRoom-{self.id}'
    

class PublicChatRoomMessage(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room            = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
    timestamp       = models.DateTimeField(auto_now_add=True)
    content         = models.TextField(unique=False, blank=False)
    
    
    def __str__(self):
        return self.user__username
    
    