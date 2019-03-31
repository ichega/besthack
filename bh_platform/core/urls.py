from django.urls import path

from .views import index_view, sign_up, post_event, sign_in, get_events, get_event, get_tasks_as_manager,get_tasks_as_perfomer


urlpatterns = [
    path('', index_view),
    path('sign_up/', sign_up),
    path('post_event/', post_event),
    path('sign_in/', sign_in),
    path('get_events/', get_events),
    path('get_profile/', get_profile),
    path('get_event/', get_event),
    path('get_tasks_as_manager/', get_tasks_as_manager),
    path('get_tasks_as_perfomer/', get_tasks_as_perfomer),

    #     # path('index', index_view),
]