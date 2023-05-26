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
    section_id = 4
    data_list = utils.get_sector(section_id)
    dict = {}
    for data in data_list:
        if data.get('sub_sector') not in dict:
            dict[data.get('sub_sector')] = data.get('pk_count')
        else:
            dict[data.get('sub_sector')] += data.get('pk_count')

    dict2={'A':3,'C':5,'D':1,"B":8}
    dict2 = sorted(list(zip(dict2.keys(), dict2.values())), key=lambda x: x[0])
    
    return render(request, 'section_4.html',{'sub_sector':dict2,'color':'#58595B'})


def detail4_D(request):
    # 4구역 D에 속하는 빌딩들 : 415, 416, 417
    dict = {}
    sector_id = 4
    subsector_id = 'D'
    location_list = utils.get_subsector(sector_id, subsector_id)
    # data => [building_num, pk_area, empty]
    for location in location_list:
        if location.get('building_num') not in dict:
            dict[location.get('building_num')] = [(location.get('pk_area'), location.get('empty'))]
        else:
            dict[location.get('building_num')].append((location.get('pk_area'), location.get('empty')))
    #dictionary에 담기는 값 => key : building_num /  value : list of 2-tuple(pk_area, empty)
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
