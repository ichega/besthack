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
from itertools import groupby




@csrf_exempt
def get_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        profile = ProfileModel.objects.filter(user=user)[0]
        data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "otch": profile.otch,
            "name": profile.name,
            "phone": profile.phone,
            "avatar": "/media/" + str(profile.image),
            "description": profile.description,
            "site": profile.site,
            "is_volon": profile.is_volon,
            "is_staff": profile.is_staff,
            "is_partner": profile.is_partner,
            }
        if profile.is_partner:
            data["inn"] = profile.inn
            data["is_phys_face"] = profile.is_phys
        return JsonResponse(data)
    else:
        return JsonResponse({
            "is_auth": "not ok"
        })


# Create your views here.


@csrf_exempt
def get_events(request):
    data = request.body.decode()
    data = json.loads(data)
    page = data["page"]
    events = EventModel.objects.all()
    events = list(events)
    #print(events)
    first = int(page)*10-10
    response = []
    for i in range(first,first+10,1):
        if i<len(events):
            event = {}
            e = events[i]
            event["id"] = e.pk
            event["name"] = e.name
            event["snippet"] = e.snippet
            event["dt_start"] = str(e.dt_start)[0:16]
            event["dt_finish"] = str(e.dt_finish)[0:16]
            event["image"] = "/media/"+str(e.image)
            event["owner"] = str(e.owner)
            response.append(event)

    return JsonResponse({"events":response})


@csrf_exempt
def get_event(request):
    data = request.body.decode()
    data = json.loads(data)
    print(data)
    event = EventModel.objects.get(pk=data["id"])
    response = {}
    response["id"]=event.pk
    response["name"] = event.name
    response["description"] = event.description
    response["dt_start"] = str(event.dt_start)[0:16]
    response["dt_finish"] = str(event.dt_finish)[0:16]
    response["image"] ="/media/" + str(event.image)
    response["owner"] = str(event.owner)

    tasks = list(TaskModel.objects.filter(event=event.pk))
    r = []
    for task in tasks:
        if task.partner != None:
            r.append(task.partner)

    r = [el for el, _ in groupby(r)]
    # print(r)
    r1 = []
    for t in r:
        q = {
            "id": User.objects.get(username=t.user).id,
            "name": t.email,
            "avatar": "/media/"+str(t.image),

        }
        r1.append(q)
    # print(r1)
    response["partners"] = r1
    return JsonResponse(response)

@csrf_exempt
def get_tasks_as_manager(request):
    data = request.body.decode()
    data = json.loads(data)
    task = TaskModel.objects.get(pk=data["id"])
    response = {}
    response["perfomer"] = str(task.perfomer)
    response["name"] = task.name
    response["description"] = task.description
    response["partner"] = str(task.partner)
    response["event"] = str(task.partner)
    response["deadline"] = str(task.deadline)[0:16]
    response["status"] = task.status
    return JsonResponse(response)

@csrf_exempt
def get_tasks_as_perfomer(request):
    perfomer = request.user
    tasks = TaskModel.objects.filter(perfomer=perfomer.pk)
    tasks = list(tasks)
    response = []
    for task in tasks:
        t = {}
        t["perfomer"] = str(task.perfomer)
        t["name"] = task.name
        t["description"] = task.description
        t["partner"] = str(task.partner)
        t["event"] = str(task.partner)
        t["deadline"] = str(task.deadline)[0:16]
        t["status"] = task.status
        response.append(t)
    return JsonResponse({"tasks":response})


@csrf_exempt
def get_partners(request):
    data = request.body.decode()
    data = json.loads(data)
    tasks = list(TaskModel.get.filter(event=data["id"]))
    response = []
    for task in tasks:
        if task.partner != None:
            response.append(task.partner)

    response = [el for el, _ in groupby(response)]

    return JsonResponse({"partners":response})






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
                           dt_finish=datetime.datetime.strptime(data["datetime_finish"], '%d.%m.%Y'),
                           image=str(filename))
        event.save
        data["id"] = event.pk
        data["image"] = str(event.image)
        assign_perm("manage", user, event)

        return JsonResponse(data)
    return JsonResponse({"code":"1"})



@csrf_exempt

def patch_event(request):
    user = request.user
    print(user)
    profile = ProfileModel.objects.filter(user=user)[0]
    if profile.is_owner:
        data = request.body.decode()
        data = json.loads(data)
        # image = data["image"].split(',')[1]
        # image_64_decode = base64.b64decode(image)
        # media_root = settings.MEDIA_ROOT
        # filename = str(uuid.uuid4()) + str("_") + str(data["image_name"])
        # path = os.path.join(media_root, filename)
        # print(path)
        # file = open(path, 'wb')
        # file.write(image_64_decode)
        event = EventModel.objects.get(id=data["id"])
        event.name=data['name']
        event.description=data['description']
        event.dt_start=datetime.strptime(data["dt_start"], '%Y-%m-%d %H:%M')
        event.dt_finish=datetime.strptime(data["dt_end"], '%Y-%m-%d %H:%M')
        # event.image=str(filename)
        event.save()
        data["id"] = event.pk
        data["image"] = str(event.image)

        return JsonResponse(data)




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


@csrf_exempt
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






@csrf_exempt
def index_view(request):
    print("Hello")
    context = {

    }
    return HttpResponse(render(request, "index.html", context))

