"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('employee_form/',views.employee_form, name="employee_form"),
    path('music/',views.music, name="music"),
    path('welcome/',views.welcome, name="welcome"),
    path('json/',views.josn_view, name="json_view"),
    path('extended_json/',views.extended_josn_view, name="extended_json_view"),
    path('extended_json2/',views.extended2_josn_view, name="extended2_josn_view"),
    # url parameter
    path('user/<str:name>', views.user_view, name="user_view"),
    # query parameter
    path('search/', views.search_view, name="search_view"),

    path('search_song/', views.song_search_view, name='song_search_view'),


    ]
