"""ChatBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ChatBot import views

urlpatterns = [
    path('',views.heropage),#as we have to call this page impicitly
    path('chatpage/',views.chatpage),#static url
    path('buttonmsg/<str:buttonName>/',views.buttonmsg,name='buttonmsg'), #dynamic url if we dont know which value will be there the dont write it
    path('subbuttonmsg/<str:corekey>/<str:content>/',views.subbuttonmsg,name='subbuttonmsg')
]
