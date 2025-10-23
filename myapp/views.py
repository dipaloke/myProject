from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse("Hello World!")
def music(request):
    return HttpResponse("Welcome to the Music App!")

# Create your views here.
