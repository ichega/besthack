from django.contrib import admin
from .models import *

admin.site.register(EventModel)
admin.site.register(TaskModel)
admin.site.register(BaseProfile)
admin.site.register(PartherProfile)
admin.site.register(StaffProfile)
admin.site.register(VolunteerProfile)
admin.site.register(ManagerProfile)



# Register your models here.
