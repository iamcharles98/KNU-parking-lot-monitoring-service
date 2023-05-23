# app_name = 'pklot'

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("", views.home),
    path("cover",views.cover),
    path("section4",views.section_4,name="section_4"), # url은 html 에서 name 으로 불려진다.

    path("detail4D",views.detail4_D,name="detail4_D"),
    path("detail4H",views.detail4_H,name="detail4_H"),
    path("detail4G",views.detail4_G,name="detail4_G"),
    path("detail4F",views.detail4_F,name="detail4_F"),
    
    path("temp/<str:id>",views.temp,name="temp"),

    

]