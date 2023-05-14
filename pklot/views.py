from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


# Create your views here.

# Create your views here.
def home(request):

    return render(request, 'home.html')

def cover(request):

    return render(request,"cover.html")