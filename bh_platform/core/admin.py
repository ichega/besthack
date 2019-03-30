from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import *

class GuardAdmin(GuardedModelAdmin):
    pass

admin.site.register(EventModel)
admin.site.register(TaskModel)
admin.site.register(ProfileModel, GuardAdmin)


# Register your models here.
