from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def union(request):
    return HttpResponse("Hello, Soviet union!")
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")