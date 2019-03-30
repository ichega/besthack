from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import json
from datetime import datetime

from guardian.shortcuts import assign_perm

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib.auth.models import User
import base64
import uuid
from django.conf import settings
import os
import json
from django.views.decorators.csrf import csrf_exempt







# Create your views here.


#
# def get_events(request):
#     data = request.body.decode()
#     data = json.loads(data)
#     page = data["page"]




@csrf_exempt
def post_event(request):
    user = request.user
    print(user)
    profile = ProfileModel.object.get(username=user)
    if profile.is_owner:
        data = request.body.decode()
        data = json.loads(data)
        image = data["image"].split(',')[1]
        image_64_decode = base64.b64decode(image)
        media_root = settings.MEDIA_ROOT
        filename = str(uuid.uuid4()) + str("_") + str(data["image_name"])
        path = os.path.join(media_root, filename)
        print(path)
        file = open(path, 'wb')
        file.write(image_64_decode)
        event = EventModel(name=data['name'], description=data['description'],
                           dt_start=datetime.datetime.strptime(data["datetime_start"], '%d.%m.%Y') ,
                           image=str(filename))
        event.save
        data["id"] = event.pk
        data["image"] = str(event.image)
        return JsonResponse(data)
    return JsonResponse({"code":"1"})



def sign_up(request):
    data = request.body.decode()
    data = json.loads(data)
    if "user_type" in data:

        user = User.objects.create(username=data['username'])
        print(data["password"])
        user.set_password(data["password"])
        user.save()

        image = data["image"].split(',')[1]
        image_64_decode = base64.b64decode(image)
        media_root = settings.MEDIA_ROOT
        filename = str(uuid.uuid4()) + str("_") + str(data["image_name"])
        path = os.path.join(media_root, filename)
        print(path)
        file = open(path, 'wb')
        file.write(image_64_decode)

        if data["user_type"]=="manager":
            profile = ProfileModel(user=user, name=data['username'], email=data['email'], phone=data["phone"], image=str(filename),
                                   description=data['short_description'],is_owner=True)
            profile.save()
            assign_perm("manage", user, profile)
            data["image"] = str(profile.image)
            data["id"] = profile.pk
            return JsonResponse(data)
        elif data["user_type"]=="volunteur":
            profile = ProfileModel(user=user, name=data['username'], email=data['email'], phone=data["phone"],
                                   image=str(filename),
                                   description=data['short_description'], is_volon=True)
            profile.save()
            assign_perm("manage", user, profile)
            data["image"] = str(profile.image)
            data["id"] = profile.pk
            return JsonResponse(data)

        elif data["user_type"]=="staff":
            profile = ProfileModel(user=user, name=data['username'], email=data['email'], phone=data["phone"],
                                   image=str(filename),
                                   description=data['short_description'], is_staff=True)
            profile.save()
            assign_perm("manage", user, profile)
            data["image"] = str(profile.image)
            data["id"] = profile.pk
            return JsonResponse(data)


        elif data["user_type"]=="phys":
            profile = ProfileModel(user=user, name=data['username'], email=data['email'], phone=data["phone"],
                                   image=str(filename),
                                   description=data['short_description'],is_partner=True, is_phys=True)
            profile.save()
            assign_perm("manage", user, profile)
            data["image"] = str(profile.image)
            data["id"] = profile.pk
            return JsonResponse(data)

        elif data["user_type"]=="ur":
            profile = ProfileModel(user=user, name=data['username'], inn=data['inn'], site=data["site_url"],
                                   image=str(filename),
                                   description=data['short_description'], is_partner=True, is_phys=False)
            profile.save()
            assign_perm("manage", user, profile)
            data["image"] = str(profile.image)
            data["id"] = profile.pk
            return JsonResponse(data)



def sign_in(request):
    data = request.body.decode()
    data = json.loads(data)
    username = data["username"]
    password = data["password"]
    is_auth = authenticate(username=username, password=password)
    if is_auth:
        return JsonResponse({
            "answer": "OK"
        })
    else:
        return JsonResponse({
            "answer": "ERROR",
        })






def index_view(request):
    print("Hello")
    context = {

    }
    return HttpResponse(render(request, "index.html", context))

