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

# section 4 가 아닌 구역에 대해서 리턴 되는 함수 
def temp(request, id):
    sample = "cover.jpeg"
    return render(request, 'temp.html', {'image': sample,'section':id})

# def section_4(request):
#     return render(request,'search.html')