from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(req):
    return render(req,"home.html")
def employee_form(req):
    return render(req,"employee_form.html")
def music(request):
    return HttpResponse("Welcome to the Music App!")
def welcome(req):
    return render(req, "welcome.html")
def josn_view(request):
    return JsonResponse({"message": "Hello!! JSON!!!"})
def extended_josn_view(request):
    return JsonResponse({"message" : 'Hello, extended JSON!', "status" : 'success', "code" : 200})
