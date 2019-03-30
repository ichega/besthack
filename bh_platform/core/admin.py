from django.contrib import admin
from .models import EventModel, TaskModel,ProfileModel

admin.site.register(EventModel)
admin.site.register(TaskModel)
admin.site.register(ProfileModel)


# Register your models here.
