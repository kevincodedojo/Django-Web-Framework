from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is  the index view of the DemoApp")

def home(request):
    return HttpResponse("<h1> Welcome to the Little Lemon! </h1>")

    