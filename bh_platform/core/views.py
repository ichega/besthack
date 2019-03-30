from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.


def get_events(request):
    
    return JsonResponse({"Hello":"World"})

def index_view(request):
    print("Hello")
    return render("index.html")