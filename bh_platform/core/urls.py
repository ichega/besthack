from django.urls import path
from .views import index_view, get_events

urlpatterns = [
    path('', index_view),
    path('get_events/', get_events),
]