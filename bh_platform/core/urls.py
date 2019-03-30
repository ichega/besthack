from django.urls import path
from .views import index_view, sign_up

urlpatterns = [
    path('', index_view),
# <<<<<<< HEAD
    path('sign_up/', sign_up),
# =======
#     # path('index', index_view),
# >>>>>>> 90ca2c92210e0a69331ea457247184591d90b7aa
]