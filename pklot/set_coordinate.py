from building import models

def initDB():
    width = 4032  # width 가 x 좌표
    height = 3024  # height 이 y 좌표
    chip_N = 17 # 반도체 융합 연구동
    it2_N = 15 # IT2호관 옆쪽 주차장

    chip_dot_info_1_14 = [[(0, 0), (0, 0)], [(42, 2977), (710, 2622)], [(177, 2632), (805, 2310)],
                     [(289, 2337), (887, 2037)], [(401, 2060), (960, 1794)], [(509, 1801), (1029, 1577)],
                     [(595, 1587), (1088, 1390)], [(670, 1403), (1144, 1212)], [(739, 1235), (1190, 1058)],
                     [(802, 1064), (1233, 913)], [(864, 920), (1276, 782)], [(1532, 2751), (2249, 2383)],
                     [(1578, 2386), (2239, 2070)], [(1624, 2090), (2242, 1797)], [(1657, 1817), (2233, 1567)]]
    chip_dot_info_15_17 = [[(3561, 1314), (3314, 1717), (3896, 1426), (3654, 1865)],
                      [(3288, 1215), (3020, 1591), (3561, 1314), (3314, 1717)],
                      [(3020, 1113), (2776, 1478), (3288, 1215), (3020, 1591)]]

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
        build1 = models.Building.objects.get(building_num=417)
        for i in range(0, chip_N+1):
            models.Pk_location(
                building_num=build1, # foreign키에 연결된 데이터를 저장하려면 연결된 테이블의 인스턴스를 넘겨줘야 된다.
                pk_area=i,
                x=center_dot[i][0],
                y=center_dot[i][1],
                w=wid[i],
                h=hei[i],
                empty=True,
            ).save()

    it2_dot_info_1_15 = [[(0, 0), (0, 0)], [(3045, 2997), (1910, 2501)], [(2992, 2573), (2015, 2218)],
                         [(2943, 2244), (2081, 2021)], [(2907, 2011), (2121, 1857)], [(2877, 1860), (2160, 1748)],
                         [(2861, 1755), (2196, 1623)], [(884, 1972), (404, 1804)], [(1029, 1820), (568, 1680)],
                         [(1153, 1694), (720, 1575)], [(1447, 1390), (1087, 1309)], [(1512, 1323), (1155, 1253)],
                         [(1574, 1256), (1226, 1197)], [(1622, 1204), (1278, 1156)], [(1710, 1111), (1413, 1069)],
                         [(1740, 1078), (1458, 1036)]]
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
        min_x = it2_dot_info_1_15[i][1][0]
        max_x = it2_dot_info_1_15[i][0][0]
        min_y = it2_dot_info_1_15[i][1][1]
        max_y = it2_dot_info_1_15[i][0][1]
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
        build2 = models.Building.objects.get(building_num=416)
        for i in range(0, it2_N + 1):
            models.Pk_location(
                building_num=build2, # foreign키에 연결된 데이터를 저장하려면 연결된 테이블의 인스턴스를 넘겨줘야 된다.
                pk_area=i,
                x=center_dot[i][0],
                y=center_dot[i][1],
                w=wid[i],
                h=hei[i],
                empty=True,
            ).save()


# def calc_coordinate(n, dot_info):
#     center_dot = []
#     wid = []
#     hei = []
