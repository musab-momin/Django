from django.urls import path, include
from . import views



app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='Register'),
    path('login/', views.LoginView.as_view(), name='Login'),
    path('logout/', views.logout, name='Logout'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='Profile'),
    path('send_request/<int:pk>/', views.SendFriendRequest.as_view(), name='SendFriendRequest'),
    path('sender_cancel_request/<int:pk_of_other>/', views.SenderCancelFriendRequest.as_view(), name='SenderCancelFriendRequest'),
    path('reciever_cancel_request/<int:sender_pk>/<int:request_id>/', views.RecieverCancelFriendRequest.as_view(), name='RecieverCancelFriendRequest'),
    path('accept_friend_request/<int:sender_pk>/<int:request_id>/', views.AcceptFriendRequest.as_view(), name='AcceptFriendRequest'),
    path('unfriend/<int:removee_id>.', views.UnFriendView.as_view(), name='UnFriend'),
    path('api/crop_and_save/', views.crop_and_save, name='CropAndSave'),
]
