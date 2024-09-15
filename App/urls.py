from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('', views.base, name='base'),
    path('contact', views.contact, name='contact'),
    
]
