from building import models

def initDB():
    # width = 4032  # width 가 x 좌표
    # height = 3024  # height 이 y 좌표
    chip_N = 17 # 반도체 융합 연구동
    it2_N = 15 # IT2호관 옆쪽 주차장
    it5_N = 12 #IT융복합관

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
    center_dot, wid, hei = calc_coordinate(417, chip_N, chip_dot_info)


    if not models.Building.objects.filter(building_num=417).exists():
        models.Building(
            building_num=417, #임시
            building_name='IT_chip', #임시
            pk_size=chip_N,
            pk_count=0,
            sector=4,
            sub_sector='F'
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
    center_dot, wid, hei = calc_coordinate(416, it2_N, it2_dot_info_1_15)

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

    it5_dot_info = [[(0, 0), (0, 0)], [(391, 792), (335, 695)], [(493, 791), (423, 691)], [(564, 790), (663, 695)],
                    [(670, 788), (754, 694)], [(777, 789), (845, 694)], [(883, 790), (930, 695)], [(153, 1271), (120, 997)],
                    [(438, 1268), (322, 994)], [(721, 1263), (553, 994)], [(720, 1263), (834, 990)], [(905, 1269), (984, 993)],
                    [(1089, 1268), (1120, 992)]]
    center_dot.clear()
    wid.clear()
    hei.clear()
    center_dot, wid, hei = calc_coordinate(415, it5_N, it5_dot_info)

    if not models.Building.objects.filter(building_num=415).exists():
        models.Building(
            building_num=415,  # 임시
            building_name='IT_5',  # 임시
            pk_size=it5_N,
            pk_count=0,
            sector=4,
            sub_sector='D'
        ).save()
    if not models.Pk_location.objects.filter(building_num__building_num=415).exists():
        build3 = models.Building.objects.get(building_num=415)
        for i in range(0, it5_N + 1):
            models.Pk_location(
                building_num=build3, # foreign키에 연결된 데이터를 저장하려면 연결된 테이블의 인스턴스를 넘겨줘야 된다.
                pk_area=i,
                x=center_dot[i][0],
                y=center_dot[i][1],
                w=wid[i],
                h=hei[i],
                empty=True,
            ).save()

    vet_dot_info = [[(0, 0), (0, 0)], [(0, 0), (0, 0)], [(2169, 3908), (2688, 3584)], [(2073, 3564), (2529, 3242)],
                    [(1962, 3212), (2398, 2965)], [(1876, 2923), (2286, 2710)], [(448, 2759), (1103, 2567)],
                    [(498, 2506), (1088, 2347)], [(534, 2293), (1074, 2161)], [(560, 2114), (1065, 1994)],
                    [(593, 1948), (1056, 1864)], [(612, 1812), (1049, 1758)], [(630, 1708), (1044, 1660)],
                    [(646, 1593), (1038, 1583)], [(658, 1502), (1035, 1485)], [(675, 1418), (1029, 1420)],
                    [(1908, 2363), (2453, 2127)], [(1880, 2123), (2391, 1919)], [(1859, 1926), (2331, 1738)],
                    [(1827, 1749), (2274, 1562)], [(1811, 1582), (2238, 1442)], [(1791, 1454), (2199, 1323)],
                    [(1775, 1332), (2162, 1213)], [(1763, 1220), (2132, 1114)], [(1747, 1119), (2104, 1018)],
                    [(1738, 1027), (2079, 941)], [(1724, 947), (2057, 867)], [(2423, 4027), (2822, 3142)],
                    [(1906, 4027), (2265, 3146)], [(1367, 4027), (1836, 3142)], [(1362, 4027), (968, 3146)],
                    [(841, 4027), (530, 3146)], [(315, 4027), (175, 3146)], [(1792, 710), (1968, 611)],
                    [(1631, 705), (1771, 607)], [(1469, 703), (1618, 602)], [(1318, 700), (1469, 599)],
                    [(1102, 2356), (550, 2108)], [(1129, 2121), (622, 1883)], [(1153, 1894), (673, 1724)],
                    [(1174, 1739), (725, 1569)], [(1194, 1587), (768, 1429)], [(1213, 1449), (801, 1309)],
                    [(1227, 1325), (845, 1183)], [(1237, 1196), (878, 1081)], [(1248, 1100), (906, 998)],
                    [(1261, 1011), (928, 923)], [(1274, 932), (950, 856)], [(1281, 865), (973, 790)],
                    [(1292, 787), (990, 719)]]
    center_dot.clear()
    wid.clear()
    hei.clear()
    center_dot, wid, hei = calc_coordinate(420, vet_N, vet_dot_info)

    if not models.Building.objects.filter(building_num=420).exists():
        models.Building(
            building_num=420,  # 임시
            building_name='수의대',  # 임시
            pk_size=vet_N,
            pk_count=0,
            sector=4,
            sub_sector='H'
        ).save()
    if not models.Pk_location.objects.filter(building_num__building_num=420).exists():
        build4 = models.Building.objects.get(building_num=420)
        for i in range(0, vet_N + 1):
            models.Pk_location(
                building_num=build4,  # foreign키에 연결된 데이터를 저장하려면 연결된 테이블의 인스턴스를 넘겨줘야 된다.
                pk_area=i,
                x=center_dot[i][0],
                y=center_dot[i][1],
                w=wid[i],
                h=hei[i],
                empty=True,
            ).save()


def calc_coordinate(building_num, n, dot_info):
    if building_num == 415:
        width = 1278
        height = 1278
    elif building_num == 420:
        width = 3019
        height = 4027
    elif building_num == 416:
        width = 4028
        height = 3020
    else:
        width = 4032  # width 가 x 좌표
        height = 3024  # height 이 y 좌표

    center_dot = []
    wid = []
    hei = []
    for i in range(0, n+1): # 중심점의 좌표를 구한다.
        ctr_x = round((dot_info[i][0][0]+dot_info[i][1][0]) / 2, 3)
        ctr_y = round((dot_info[i][0][1]+dot_info[i][1][1]) / 2, 3)
        x_ratio = round(ctr_x / width, 6)  # rouond : 반올림해서 6번째 자리까지 나타냄
        y_ratio = round(ctr_y / height, 6)
        center_dot.append((x_ratio, y_ratio))

    for i in range(0, n+1): # 폭과 너비를 구한다.
        max_x = dot_info[i][1][0]
        min_x = dot_info[i][0][0]
        max_y = dot_info[i][1][1]
        min_y = dot_info[i][0][1]
        w = max_x - min_x if min_x <= max_x else min_x - max_x
        h = max_y - min_y if min_y <= max_y else min_y - max_y
        w_ratio = round(w / width, 6)
        h_ratio = round(h / height, 6)
        wid.append(w_ratio)
        hei.append(h_ratio)

    return center_dot, wid, hei
