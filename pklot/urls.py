# app_name = 'pklot'

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("", views.home),
    path("cover",views.cover)
]