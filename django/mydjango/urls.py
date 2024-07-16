"""
URL configuration for mydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from .views import*
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello form the other side!! ")

# def about(request):
#     return HttpResponse("Okay have a great time !!!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('myapp/',include('myapp.urls')),
    path('base/',about),
    path('service/',service),
    path('dynamic/',dynamic),
    path('add/<int:a>/<int:b>/',add)
]
