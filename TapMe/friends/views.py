import email
from django.shortcuts import render
from django.views.generic import ListView
import account
from friends.models import FriendList
from account.models import Account

# Create your views here.
class FriedListView(ListView):
    model = FriendList
    template_name = 'friends/friend_list.html'

    def get_queryset(self):
        queryset = FriendList.objects.get(user__pk =  self.request.resolver_match.kwargs['pk'])
        print(f'''
          This is the friendlist {queryset.friend_lst.all()}
          
          ''')
        return queryset.friend_lst.all()
    
    def get_context_data(self, **kwargs):
        context = super(FriedListView, self).get_context_data(**kwargs)
        context['title'] = 'Friend List'
        context['loggedin_user_profile_image'] = self.request.user.profile_image
        context['loggedin_user_id'] = self.request.user.id
        print(f'''
              This is context {context}
              
              ''')
        return context