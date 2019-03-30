<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
=======
from django.shortcuts import render, HttpResponse
>>>>>>> 90ca2c92210e0a69331ea457247184591d90b7aa

# Create your views here.


def get_events(request):
    
    return JsonResponse({"Hello":"World"})

def index_view(request):
    print("Hello")
    context = {

    }
    return HttpResponse(render(request, "index.html", context))