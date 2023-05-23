from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from pklot import utils


# Create your views here.

# Create your views here.
def home(request):
    return render(request, 'home.html')


def cover(request):
    return render(request, "cover.html")


def section_4(request):
    data_list = utils.get_sector(4)
    dict = {}
    for data in data_list:
        if data.get('sub_sector') not in dict:
            dict[data.get('sub_sector')] = data.get('pk_count')
        else:
            dict[data.get('sub_sector')] += data.get('pk_count')
    return render(request, 'section_4.html', {'data': dict})


def detail4_D(request):
    return render(request, 'detail4_D.html')


def detail4_H(request):
    return render(request, 'detail4_H.html')


def detail4_G(request):
    return render(request, 'detail4_G.html')


def detail4_F(request):
    return render(request, 'detail4_F.html')


# 필요하지않은  구역에 대해서 리턴 되는 함수
def temp(request, id):
    sample = "cover.jpeg"
    return render(request, 'temp.html', {'image': sample, 'section': id})

# def section_4(request):
#     return render(request,'search.html')
