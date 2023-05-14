# app_name = 'pklot'

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("", views.home),
    path("cover",views.cover),
    path("section3",views.section_3,name="section_3"),
    path("section4",views.section_4,name="section_4"),
    # path('', home, name='home'),
    # path('detail/<str:id>',detail, name="detail"),
    path("search/<str:id>",views.search,name="search")
]