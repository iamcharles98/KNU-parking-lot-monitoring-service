from building import models
from building.models import Building, Pk_location


def initDB():
    width = 4032  # width 가 x 좌표
    height = 3024  # height 이 y 좌표
    chip_N = 17
    it2_N = 15

    chip_dot_info_1_14 = [[(0, 0), (0, 0)], [(42, 2977), (710, 2622)], [(177, 2632), (805, 2310)],
                     [(289, 2337), (887, 2037)], [(401, 2060), (960, 1794)], [(509, 1801), (1029, 1577)],
                     [(595, 1587), (1088, 1390)], [(670, 1403), (1144, 1212)], [(739, 1235), (1190, 1058)],
                     [(802, 1064), (1233, 913)], [(864, 920), (1276, 782)], [(1532, 2751), (2249, 2383)],
                     [(1578, 2386), (2239, 2070)], [(1624, 2090), (2242, 1797)], [(1657, 1817), (2233, 1567)]]
    chip_dot_info_15_17 = [[(3020, 1113), (2776, 1478), (3288, 1215), (3020, 1591)],
                      [(3288, 1215), (3020, 1591), (3561, 1314), (3314, 1717)],
                      [(3561, 1314), (3314, 1717), (3896, 1426), (3654, 1865)]]


    for i in range(3):
        x_dot = sorted(chip_dot_info_15_17[i], key=lambda x: (x[0]))  # x축을 기준으로 오름차순
        y_dot = sorted(chip_dot_info_15_17[i], key=lambda x: (x[1]))  # y축을 기준으로 오름차순
        chip_dot_info_15_17[i] = [(x_dot[0][0], y_dot[0][1]), (x_dot[-1][0], y_dot[-1][1])]

    chip_dot_info = chip_dot_info_1_14 + chip_dot_info_15_17
    center_dot = []
    wid = []
    hei = []
    for i in range(0, chip_N+1): # 중심점의 좌표를 구한다.
        ctr_x = round((chip_dot_info[i][0][0]+chip_dot_info[i][1][0]) / 2, 3)
        ctr_y = round((chip_dot_info[i][0][1]+chip_dot_info[i][1][1]) / 2, 3)
        x_ratio = round(ctr_x / width, 6)  # rouond : 반올림해서 6번째 자리까지 나타냄
        y_ratio = round(ctr_y / height, 6)
        center_dot.append((x_ratio, y_ratio))

    for i in range(0, chip_N+1): # 폭과 너비를 구한다.
        max_x = chip_dot_info[i][1][0]
        min_x = chip_dot_info[i][0][0]
        max_y = chip_dot_info[i][1][1]
        min_y = chip_dot_info[i][0][1]
        w = max_x - min_x if min_x <= max_x else min_x - max_x
        h = max_y - min_y if min_y <= max_y else min_y - max_y
        w_ratio = round(w / width, 6)
        h_ratio = round(h / height, 6)
        wid.append(w_ratio)
        hei.append(h_ratio)

    if not models.Building.objects.filter(building_num=417).exists():
        models.Building(
            building_num=417, #임시
            building_name='IT_chip', #임시
            pk_size=chip_N,
            pk_count=0,
            sector=4,
            sub_sector='D'
        ).save()

    if not models.Pk_location.objects.filter(building_num__building_num=417).exists():
        bnum = Building.objects.get(building_num=417)
        for i in range(0, chip_N+1):
            models.Pk_location(
                building_num=bnum,
                pk_area=i,
                x=center_dot[i][0],
                y=center_dot[i][1],
                w=wid[i],
                h=hei[i],
                empty=False,
            ).save()

    it2_dot_info_1_15 = [[(0, 0), (0, 0)], [(1775, 2918), (2992, 2586)], [(1914, 2534), (2973, 2281)],
                         [(2002, 2218), (2930, 2054)], [(2071, 2011), (2894, 1880)], [(2131, 1843), (2864, 1755)],
                         [(2163, 1742), (2851, 1640)], [(191, 1956), (1032, 1818)], [(402, 1800), (1154, 1691)],
                         [(571, 1679), (1261, 1584)], [(982, 1381), (1512, 1316)], [(1079, 1311), (1571, 1256)],
                         [(1150, 1254), (1622, 1203)], [(1227, 1199), (1666, 1160)], [(1364, 1109), (1743, 1079)],
                         [(1419, 1076), (1773, 1050)]]
    center_dot.clear()
    wid.clear()
    hei.clear()
    for i in range(0, it2_N + 1):
        ctr_x = round((it2_dot_info_1_15[i][0][0] + it2_dot_info_1_15[i][1][0]) / 2, 3)
        ctr_y = round((it2_dot_info_1_15[i][0][1] + it2_dot_info_1_15[i][1][1]) / 2, 3)
        x_ratio = round(ctr_x / width, 6)  # rouond : 반올림해서 6번째 자리까지 나타냄
        y_ratio = round(ctr_y / height, 6)
        center_dot.append((x_ratio, y_ratio))

    for i in range(0, it2_N + 1):
        max_x = it2_dot_info_1_15[i][1][0]
        min_x = it2_dot_info_1_15[i][0][0]
        max_y = it2_dot_info_1_15[i][1][1]
        min_y = it2_dot_info_1_15[i][0][1]
        w = max_x - min_x if min_x <= max_x else min_x - max_x
        h = max_y - min_y if min_y <= max_y else min_y - max_y
        w_ratio = round(w / width, 6)
        h_ratio = round(h / height, 6)
        wid.append(w_ratio)
        hei.append(h_ratio)

    if not models.Building.objects.filter(building_num=416).exists():
        models.Building(
            building_num=416,  # 임시
            building_name='IT_2',  # 임시
            pk_size=it2_N,
            pk_count=0,
            sector=4,
            sub_sector='D'
        ).save()

    if not models.Pk_location.objects.filter(building_num__building_num=416).exists():
        bnum = Building.objects.get(building_num=416)
        for i in range(0, it2_N + 1):
            models.Pk_location(
                building_num=bnum,
                pk_area=i,
                x=center_dot[i][0],
                y=center_dot[i][1],
                w=wid[i],
                h=hei[i],
                empty=False,
            ).save()


# def calc_coordinate(n, dot_info):
#     center_dot = []
#     wid = []
#     hei = []
