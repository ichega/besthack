from django.shortcuts import render, HttpResponse

# Create your views here.


def index_view(request):
    print("Hello")
    context = {

    }
    return HttpResponse(render(request, "index.html", context))