from logging import exception
from pyexpat import model
from django.views.generic.list import ListView
from django.shortcuts import render,redirect
from django.views import View

import account
from .models import Account
from django.contrib import auth
from .forms import RegistrationForm, UpdateAccountForm
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.conf import settings
from friends.models import FriendList, FriendRequest
from friends.utils import get_friend_request_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#imports for image cropping
from account.utils import save_tmp_profile_image_from_base64string
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import os
import cv2
import json
import base64
import requests
from django.core import files

# Create your views here.
class RegisterView(View):
    context = {
        'title' : 'Register'
    }
    def get(self, request):
        return render(request, 'account/register.html', self.context)

    def post(self, request):
        reg_frm = RegistrationForm(request.POST)
        
        if reg_frm.is_valid():
            email = reg_frm.cleaned_data['email']
            username = reg_frm.cleaned_data['username']
            password = reg_frm.cleaned_data['password']
            obj = Account.objects.create_user(email, username, password)
            messages.info(request, 'You are registered succesfully!')
        else:
            self.context['reg_frm'] = reg_frm

        return redirect('/account/register/')


class LoginView(View):
    context = {
        'title' : 'Login'
    }
    def get(self, request):
        return render(request, 'account/login.html', self.context)
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        account = Account.objects.filter(email=email)

        if account.exists():
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Bad Credentials')
                return redirect('/account/login/')

        else:
            messages.info(request, 'User does not exists')
            return redirect('/account/login/')

        

def logout(request):
    auth.logout(request)
    return redirect('/account/login')


class ProfileView(LoginRequiredMixin, View):
    __context = {
        'title' : 'profile'
    }
    def get(self, request, pk):
        try:
            account = Account.objects.get(id=pk)
            self.__context['active_user'] = account
            login_user = request.user
            '''
                active_user = The user whoes profile we are visiting
                Logic for profile page
                is_self = False
                    is_friend = False
                        no_request_sent = -1
                        other_sent_to_you = 0
                        you_sent_to_other = 1
            '''
            #setting up the state variables on this variables we manipulate the front end
            is_self = True
            is_other = True
            is_friend = False
            hide_email = account.hide_email
        
            try:
                #getting the friend list of active user
                frnd_lst = FriendList.objects.get(user=account)
            except Exception as ex:
                #creating a friend list for active user bcoz every user must have a friend list
                frnd_lst = FriendList.objects.create(user=account)
                frnd_lst.save()

            active_user_frnd_lst = frnd_lst.friend_lst.all()
            self.__context['total_friends'] = len(active_user_frnd_lst)
            if request.user == account:
                is_other = False
            elif request.user != account:
                is_self = False
                if active_user_frnd_lst.filter(pk=login_user.id):
                    is_friend = True
                else:
                    is_friend = False
                    friend_request_from_other = get_friend_request_or_404(account, login_user)

                    if friend_request_from_other != False:
                        friend_request_id = friend_request_from_other.pk
                        self.__context['friend_request_id'] = friend_request_id
                        self.__context['other_sent_to_you'] = True
                        self.__context['you_sent_to_other'] = False 
                    else:
                        self.__context['other_sent_to_you'] = False
                        friend_request_from_you = get_friend_request_or_404(login_user, account)
                        
                        if friend_request_from_you != False:
                            self.__context['you_sent_to_other'] = True 
                        else:
                          self.__context['you_sent_to_other'] = False  
                               
            
        
            self.__context['is_self'] = is_self
            self.__context['is_other'] = is_other
            self.__context['is_friend'] = is_friend
            self.__context['hide_email'] = hide_email
            self.__context['loggedin_user_id'] = login_user.id
            self.__context['loggedin_user_profile_image'] = login_user.profile_image

            print(f'''
                This is the context {self.__context}
            ''')

            return render(request, 'account/profile.html', self.__context)
        except Exception as ex:
            print(f'''
                Got the exception on profile view:\n {ex}
            ''')
            return redirect('/account/register/')
    

    def post(self, request, pk):
        try:
            account = Account.objects.get(id=pk)
        except Account.DoesNotExist:
            return HttpResponse('Something went wrong')

        #this is for edge case for somehow user manage to update another user profile so we have to stop it
        if request.user.pk != account.pk:
            return HttpResponse('It is not your profile')
        
        #by setting instance to request.user we link our form to the logged in user so that when we call the save method 
        #it will update the same instance don't create new one
        update_form = UpdateAccountForm(request.POST, request.FILES, instance=request.user)

        if update_form.is_valid():
            # account.profile_image.delete()  #we are deleting the previouse image
            update_form.save()
            print('form is saved')
            return redirect(f'/account/profile/{pk}')

        else:
            # self.__context['update_frm'] = update_form
            for field in update_form:
                for error in field.errors:
                    print('I am printing this error', error)
        
        return redirect(f'/account/profile/{pk}')



class SendFriendRequest(LoginRequiredMixin, View):
    def get(self, request, pk):
        context = {}
        #login user is sending the request 
        sender = request.user
        #to the user whos profile is acitve
        try:
            reciever = Account.objects.get(id=pk)
            request_obj = FriendRequest.objects.create(sender=sender, receiver=reciever)
        except Exception as ex:
            print(f'''
                Exception while fetching reciever\n{ex}
            ''')
        
        return redirect(f'/account/profile/{pk}/')


class SenderCancelFriendRequest(LoginRequiredMixin, View):
    def get(self, request, pk_of_other):
        try:
            reciever = Account.objects.get(id=pk_of_other)
            sended_friend_request = FriendRequest.objects.filter(sender=request.user, receiver=reciever)     #fetching the request which login user sended
            
            #this is a edge case if there is more than 1 request for same users
            if len(sended_friend_request) > 1:
                for request in sended_friend_request:
                    request.rejected_by_sender()
            #normaly deleting the friend requeset
            else:        
                sended_friend_request.first().rejected_by_sender()

        except Exception as ex:
            print(f'''
                Got the exception while trying to cancel the friend request
            ''')
        return redirect(f'/account/profile/{pk_of_other}/')


class RecieverCancelFriendRequest(LoginRequiredMixin, View):
    def get(self, request,sender_pk, request_id):
        user = request.user
        try:
            recieved_friend_request = FriendRequest.objects.get(pk=request_id)
        except Exception as ex:
            print(f'''
                Got the exception while fetching the friend request {ex}
            ''')

        if recieved_friend_request.receiver == user:
            recieved_friend_request.rejected_by_reciever()
        
        return redirect(f'/account/profile/{sender_pk}/')


class AcceptFriendRequest(LoginRequiredMixin, View):
    def get(self, request, sender_pk, request_id):
        user = request.user
        try:
            recieved_friend_request = FriendRequest.objects.get(pk=request_id)
            if recieved_friend_request.is_active and recieved_friend_request.receiver == user:
                recieved_friend_request.accept_request()
        except Exception as ex:
            print(f'''
                Got the exception while accepting the friend request {ex}
            ''')
        
        return redirect(f'/account/profile/{sender_pk}/')
            

class UnFriendView(LoginRequiredMixin, View):
    def get(self, request, removee_id):
        user = request.user
        
        login_user = FriendList.objects.get(user=user)
        try:
            other_user_account = Account.objects.get(pk=removee_id)
        except Exception as ex:
            print(f'''
                User whom with you are trying to terminate friendship is not present:\n{ex}
            ''')

        login_user_frnd_lst = login_user.friend_lst.all()

        if other_user_account in login_user_frnd_lst:
            login_user.unfriend(other_user_account)
        else:
            print('Something went wrong....')
        
        return redirect(f'/account/profile/{removee_id}')


class FriendListView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        context = {}
        try:
            active_user = FriendList.objects.get(user__pk = user_id)
            frnd_lst = active_user.friend_lst.all()
            context['frnd_lst'] = frnd_lst
        except exception as ex:
            print(f'''
                Got the exception while fetch friend list
                \n{ex}
            ''') 

        return redirect(f'/account/profile/{user_id}/')


@api_view(['POST'])
def crop_and_save(request):
    payload = {}
    try:
        user_id = request.data['userId']
        user = Account.objects.get(pk=user_id)
        image_string = request.data['image'] #we are sending the image in string format with base64
        url = save_tmp_profile_image_from_base64string(image_string, user) #temporarly saving that image inside temp folder
        
        print(f'''
            {url}
        ''')
        img = cv2.imread(url) #using open cv to read the temp profile image we just stored
        
        #these are values which we sent from front end
        cropX = int(float(str(request.data['cropX'])))      
        cropY = int(float(str(request.data['cropY'])))
        cropWidth = int(float(str(request.data['cropWidth'])))
        cropHeight = int(float(str(request.data['cropHeight'])))

        #handling the cropper js bug
        if cropX < 0:   cropX = 0
        if cropY < 0:   cropY = 0


        crop_img = img[cropY:cropY + cropHeight, cropX:cropX+cropWidth]         #croping the image
        cv2.imwrite(url, crop_img)                                              #overriding the image temp image with croped one

        user.profile_image.delete()
        user.profile_image.save('profile_image', files.File(open(url, 'rb')))         #saving the profile image in actual folder
        user.save()

        payload['result'] = 'success'                                           
        payload['cropped_profile_image'] = user.profile_image.url

        os.remove(url)
                                                                 
        return Response([payload], status.HTTP_200_OK)

    except Exception as ex:
        print(ex)
        return Response(['Something went wrong'], status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    return Response(['WELCOME TO THIS END POINT OF API'], status=status.HTTP_200_OK)



