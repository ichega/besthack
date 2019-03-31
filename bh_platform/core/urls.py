from django.urls import path
from .views import index_view, sign_up, post_event, sign_in, get_events

urlpatterns = [
    path('', index_view),
    path('sign_up/', sign_up),
    path('post_event/', post_event),
    path('sign_in/', sign_in),
    path('get_events/', get_events),

#     # path('index', index_view),
]