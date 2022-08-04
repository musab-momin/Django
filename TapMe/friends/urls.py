from django.urls import path
from . import views


app_name = 'Friends'

urlpatterns = [
    path('list/<int:pk>', views.FriedListView.as_view(), name='FriendList')
]
 