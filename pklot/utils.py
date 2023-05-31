from django.http import Http404
from django.shortcuts import get_object_or_404
from building.models import Building, Pk_location
from pklot.serializers import buildingSerializers, locationSerializers
import os


def get_sector(sector_id):
    buildings = Building.objects.filter(sector=sector_id)
    if buildings.count() == 0:
        raise Http404("No Building")
        return
    else:
        serializer = buildingSerializers(buildings, many=True)
        return serializer.data


def get_subsector(sector_id, subsector_id):
    building = Building.objects.filter(sector=sector_id, sub_sector=subsector_id)
    building_num_list = []
    for b in building:
        building_num_list.append(b.building_num)
    locations = Pk_location.objects.filter(building_num__in=building_num_list)
    if locations.count() == 0:
        return Http404("No Location")
    else:
        serializer = locationSerializers(locations, many=True)
        return serializer.data


def update_pklocation(result, num):
    location_set = Pk_location.objects.filter(building_num=num)
    building = get_object_or_404(Building, building_num=num)

    if location_set.count() == 0:
        return Http404("Building_num is Wrong")
    else:
        update_list = []
        update_list2 = []
        for location in location_set:
            if num == 420 and location.pk_area not in [27, 28, 29, 30, 31, 32]:
                continue

            Xmin = location.x - location.w / 2
            Xmax = location.x + location.w / 2
            Ymin = location.y - location.h / 2
            Ymax = location.y + location.h / 2

            for el in result:
                x, y = el[1], el[2]
                if Xmin <= x <= Xmax and Ymin <= y <= Ymax:
                    location.empty = False
                    update_list.append(location)

        for location in location_set:
            if num == 420 and location.pk_area not in [27, 28, 29, 30, 31, 32]:
                continue

            if location not in update_list:
                location.empty = True
                update_list2.append(location)

        building.pk_count = building.pk_size - len(update_list)
        if building.pk_count <= building.pk_size:
            building.save()
        Pk_location.objects.bulk_update(update_list2, ['empty'])
        Pk_location.objects.bulk_update(update_list, ['empty'])


def adjacent_priority_algorithm(result, num):
    # 전체 주차 공간 불러 오기
    parking_area = Pk_location.objects.filter(building_num=num)
    building = get_object_or_404(Building, building_num=num)

    if parking_area.count() == 0:
        return Http404("Building_num is Wrong")
    else:
        update_list = []
        update_list2 = []
        check = [False for _ in range(building.pk_size + 1)]
        # label[1] : x, label[2] : y, label[3] : w, label[4] : h
        for label in result:
            lx, ly, lw, lh = label[1], label[2], label[3], label[4]
            lx_min = lx - lw / 2
            lx_max = lx + lw / 2
            ly_min = ly + lh / 2
            ly_max = ly - lh / 2

            include = []
            temp = []
            # 라벨 안에 포함 되는 주차 구역 구하기
            for pk in parking_area:
                if num == 420 and pk.pk_area in [27, 28, 29, 30, 31, 32]:
                    continue

                px, py, pw, ph = pk.x, pk.y, pk.w, pk.h
                points = [[px + pw / 2, py], [px - pw / 2, py], [px, py + ph / 2], [px, py - ph / 2]]

                for point in points:
                    if lx_min < point[0] < lx_max and ly_max < point[1] < ly_min:
                        include.append(pk)
                        temp.append(pk.pk_area)
                        break

            # 포함된 구역이 없으면 넘어가기
            if len(include) == 0:
                continue
            else:
                # 포함 되는 주차 구역 중에서 라벨의 밑변과 가장 가까운 구역 찾기 -> y 좌표 이요
                min_distance = float("inf")
                area = -1
                for pk in include:

                    y_min = pk.y + pk.h / 2
                    distance = abs(ly_min - y_min)

                    if distance < min_distance:
                        min_distance = distance
                        area = pk.pk_area

                # 최종 결과값 넣기
                for pk in parking_area:
                    if area == pk.pk_area and check[area] is False:
                        check[area] = True
                        pk.empty = False
                        update_list.append(pk)
                        break

        for pk in parking_area:
            if num == 420 and pk.pk_area in [27, 28, 29, 30, 31, 32]:
                continue

            if pk not in update_list:
                pk.empty = True
                update_list2.append(pk)

        building.pk_count = building.pk_size - len(update_list)

        if building.pk_count <= building.pk_size:
            building.save()

        Pk_location.objects.bulk_update(update_list2, ['empty'])
        Pk_location.objects.bulk_update(update_list, ['empty'])


def change_file(building_num):
    # occupied 만 존재 하도록 파일을 변경

    dir_path = f'YOLO_model/yolov5/runs/detect/{str(building_num)}/result/labels'

    files = sorted(os.listdir(dir_path))
    if len(files) > 0:
        latest_file = files[len(files) - 1]
        file_path = os.path.join(dir_path, latest_file)

    # Open the file for reading and writing
    with open(file_path, 'r+') as file:
        # Read the lines from the file
        lines = file.readlines()

        # Move the file pointer to the beginning of the file
        file.seek(0)

        # Iterate over the lines
        for line in lines:
            # Split the line into individual elements
            elements = line.split()

            # Check if the first element is not 0
            if int(elements[0]) != 0:
                # Write the line back to the file
                file.write(line)

        # Truncate the remaining content (if any) after the last valid line
        file.truncate()


def read_rows_from_file(file_path):
    rows = []  # Initialize an empty list to store the rows

    with open(file_path, 'r') as file:
        for line in file:
            row = [float(element) for element in line.strip().split()]  # Convert elements to float
            rows.append(row)  # Add the row to the list

    return rows
