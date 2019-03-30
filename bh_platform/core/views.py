from django.shortcuts import render

# Create your views here.


def index_view(request):
    print("Hello")
    return render("index.html")