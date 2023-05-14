from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


# Create your views here.

# Create your views here.
def home(request):

    return render(request, 'home.html')

def cover(request):

    return render(request,"cover.html")


def section_4(request):
    return render(request,'section_4.html')

def section_3(request):
    return render(request,'section_3.html')


def search(request, id):
    sample = "cover.jpeg"
    return render(request, 'temp.html', {'image': sample,'section':id})

# def section_4(request):
#     return render(request,'search.html')