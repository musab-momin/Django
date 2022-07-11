from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class FriendList(models.Model):
    user            = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friend_lst      = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_query_name='friends')


    def __str__(self):
        return self.user.username

    #adding user in our friend list
    def add_friend(self, account):
        if not account in self.friend_lst.all():
            self.friend_lst.add(account)
            self.save()

    #removing user from our firend list
    def remove_friend(self, account):
        if account in self.friend_lst.all():
            self.friend_lst.remove(account)
            self.save()
    
    
    def unfriend(self, removee):    
        ''' 
            here remover is the user who is terminating the friendship
            and removee is ther user to whom with remover is terminating the friendship
        '''
        remover_friend_lst = self            
        remover_friend_lst.remove_friend(removee) #removing the friend from remover's friends list

        removee_friend_lst = FriendList.objects.get(user=removee)   #removing the frind from removee friends list
        removee_friend_lst.remove_friend(self.user)


    def is_friends(self, friend):
        if friend in self.friend_lst.all():
            return True
        return False



    
    
class FriendRequest(models.Model):
    sender          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    is_active       = models.BooleanField(default=True, blank=True, null=False)
    timestamp       = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.sender.username


    def accept_request(self):
        sender_friend_lst   = FriendList.objects.get(user=self.sender)
        receiver_friend_lst = FriendList.objects.get(user=self.receiver)
        
        if sender_friend_lst:
            sender_friend_lst.add_friend(self.receiver)
            if receiver_friend_lst:
                receiver_friend_lst.add_friend(self.sender)
                self.is_active = False
                self.save()
        

    #if a user who get the request wants to reject the request then call this method    
    def rejected_by_reciever(self):
        self.is_active = False    
        self.save()
    

    #if a user who sends the reqeust wants to withdraw the request then call this mehtod
    def rejected_by_sender(self):
        self.is_active = False
        self.save()