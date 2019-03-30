from django.urls import path
from .views import index_view, get_events

urlpatterns = [
    path('', index_view),
<<<<<<< HEAD
    path('get_events/', get_events),
=======
    # path('index', index_view),
>>>>>>> 90ca2c92210e0a69331ea457247184591d90b7aa
]