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
def extended2_josn_view(request):
    return JsonResponse({"message" : 'Hello, JSON!'})

# URL parameter
def user_view(request, name):
    color = request.GET.get('color','')
    return HttpResponse(f"Hello, {name}!, Your favorite color, {color}")

# query parameter
def search_view(request):
    query = request.GET.get('q', '')
    return HttpResponse(f'You have searched for: {query}')

def song_search_view(request):
    song = request.GET.get('song', '')
    return HttpResponse(f'You searched for: {song}')
