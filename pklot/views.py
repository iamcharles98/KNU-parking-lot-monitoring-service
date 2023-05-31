from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from building.models import Building
from pklot import utils


RED= '#F38282'
GREEN = '#C7FF80'
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

    sub_a = dict.get('A')
    sub_b = dict.get('B')
    sub_c = dict.get('C')
    sub_d = dict.get('D')
    sub_e = dict.get('E')
    sub_f = dict.get('F')
    sub_g = dict.get('G')
    sub_h = dict.get('H')
    '''
    구역 log
    print(dict)
    '''
    return render(request, 'section_4.html',{'sub_sector_a':sub_a,
                                             'sub_sector_b':sub_b,
                                             'sub_sector_c':sub_c,
                                             'sub_sector_d':sub_d,
                                             'sub_sector_e':sub_e,
                                             'sub_sector_f':sub_f,
                                             'sub_sector_g':sub_g,
                                             'sub_sector_h':sub_h, 
                                             'color':'#58595B'})


def detail4_D(request):
    # 4구역 D에 속하는 빌딩들 : 415, 416
    dict = {}
    sector_id = 4
    subsector_id = 'D'
    color = GREEN
    location_list = utils.get_subsector(sector_id, subsector_id)
    building = get_object_or_404(Building, building_num=415)
    # data => [building_num, pk_area, empty]
    for location in location_list:
        if location.get('empty'):
               color = GREEN
        else:
           color = RED
        if location.get('building_num') not in dict:
            dict[location.get('building_num')] = [(location.get('pk_area'), color)]
        else:
            dict[location.get('building_num')].append((location.get('pk_area'),color))
    '''
    건물 정보 log
    print("416 건물 정보는 :", dict.get(416))
    print("\n")
    print("415 건물 정보는 :", dict.get(415))
    '''
    #dictionary에 담기는 값 => key : building_num /  value : list of 2-tuple(pk_area, empty) 'current_time':loca
    return render(request, 'detail4_D.html',{'location_info_416':dict.get(416),'location_info_415':dict.get(415), 'current_time':building.modifiedAt})



def detail4_H(request):

     # 4구역 H에 속하는 빌딩들 : 420
    dict = {}
    sector_id = 4
    subsector_id = 'H' # 원래는 F 가 맞음
    color = GREEN
    location_list = utils.get_subsector(sector_id, subsector_id)
    building = get_object_or_404(Building, building_num=420)


# data => [building_num, pk_area, empty]
    for location in location_list:
        if location.get('empty'):
               color = GREEN
        else:
           color = RED
        if location.get('building_num') not in dict:
            dict[location.get('building_num')] = [(location.get('pk_area'), color)]
        else:
            dict[location.get('building_num')].append((location.get('pk_area'),color))
    '''
    건물 정보 log
    print("420 건물 정보는 :", dict.get(420))
    print('\n')
    '''
    #dictionary에 담기는 값 => key : building_num /  value : list of 2-tuple(pk_area, empty)
    return render(request, 'detail4_H.html',{'location_info_420':dict.get(420),'current_time':building.modifiedAt})



def detail4_G(request):
     # 4구역 G에 속하는 빌딩들 : 418
    dict = {}
    sector_id = 4
    subsector_id = 'D'
    color = GREEN
    location_list = utils.get_subsector(sector_id, subsector_id)
    # data => [building_num, pk_area, empty]
    for location in location_list:
        if location.get('empty'):
               color = GREEN
        else:
           color = RED
        if location.get('building_num') not in dict:
            dict[location.get('building_num')] = [(location.get('pk_area'), color)]
        else:
            dict[location.get('building_num')].append((location.get('pk_area'),color))
    '''
    건물 정보 log 
    print("418 건물 정보는 :", dict.get(418))
    print('\n')
    '''
    #dictionary에 담기는 값 => key : building_num /  value : list of 2-tuple(pk_area, empty)
    return render(request, 'detail4_G.html',{'location_info_418':dict.get(418),})
   


def detail4_F(request):
    # 4구역 F에 속하는 빌딩들 : 417
    dict = {}
    sector_id = 4
    subsector_id = 'F' # 원래는 F 가 맞음
    color = GREEN
    location_list = utils.get_subsector(sector_id, subsector_id)
    building = get_object_or_404(Building, building_num=417)

    # data => [building_num, pk_area, empty]
    for location in location_list:
        if location.get('empty'):
               color = GREEN
        else:
           color = RED
        if location.get('building_num') not in dict:
            dict[location.get('building_num')] = [(location.get('pk_area'), color)]
        else:
            dict[location.get('building_num')].append((location.get('pk_area'),color))
    '''
    건물 정보 log
    print("417 건물 정보는 :", dict.get(417))
    print('\n')
    '''
    #dictionary에 담기는 값 => key : building_num /  value : list of 2-tuple(pk_area, empty)
    return render(request, 'detail4_F.html',{'location_info_417':dict.get(417),'current_time':building.modifiedAt})
     


# 필요하지않은  구역에 대해서 리턴 되는 함수
def temp(request, id):
    sample = "cover.jpeg"
    return render(request, 'temp.html', {'image': sample, 'section': id})

# def section_4(request):
#     return render(request,'search.html')
