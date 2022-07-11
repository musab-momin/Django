from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import os
import cv2
import json
import base64
import requests
from django.core import files



def save_tmp_profile_image_from_base64string(image_string, user):
    INCORRECT_PADDING_EXCEPTION = 'Incorect padding'
    TEMP_PROFILE_IMAGE_NAME = "tmp_profile_image.png"
    # print(f'''
    #     This is image string {image_string}
    #     This is user {user}
    
    # ''')
    try:
        
        #cheking that temp folder exists in media_cdn folder this settings.TEMP I wrote this variable inside settings.py file
        if not os.path.exists(settings.TEMP):
            os.mkdir(settings.TEMP)                            #if folder is not present then we are creating it
        #cheking that inside temp folder there is specific folder for each user based on it's primary key
        if not os.path.exists(f'{settings.TEMP}\\{user.pk}'):
            os.mkdir(f'{settings.TEMP}\\{user.pk}')              #if folder is not present then we are creating it
        
        url = os.path.join(f"{settings.TEMP}\\{user.pk}", TEMP_PROFILE_IMAGE_NAME) #getting the file location
        storage = FileSystemStorage(location=url)               #using file system to read that file
        image = base64.b64decode(image_string)                  

        with storage.open('', 'wb+') as destination:
            destination.write(image)
            destination.close()
        return url

    except Exception as ex:
        print('got an exception', ex)
        if str(ex) == INCORRECT_PADDING_EXCEPTION:
            image_string += '=' * ((4-len(image_string)%4)%4)
            return save_tmp_profile_image_from_base64string(image_string, user)
    return None
