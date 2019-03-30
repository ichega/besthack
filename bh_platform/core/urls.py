from django.urls import path
from .views import index_view

urlpatterns = [
    path('', index_view),
    # path('index', index_view),
]