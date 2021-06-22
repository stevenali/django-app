from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('contact',views.contact),
    path('gönder',views.contactbackend, name="contactbackend"),
]
