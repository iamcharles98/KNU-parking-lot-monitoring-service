from django.http import Http404

from cctv import views
from building.models import Building, Pk_location
from pklot.serializers import buildingSerializers, locationSerializers
from django.core.exceptions import ObjectDoesNotExist
import math, os

"""예외 처리 필요"""


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
    if location_set.count() == 0 :
        return Http404("Building_num is Wrong")
    else:
        update_list = []
        for location in location_set:
            Xmin = location.x - location.w / 2
            Xmax = location.x + location.w / 2
            Ymin = location.y - location.h / 2
            Ymax = location.y + location.h / 2
            for el in result:
                x, y = el[1], el[2]
                if Xmin <= x <= Xmax and Ymin <= y <= Ymax:
                    location.empty = False
                    update_list.append(location)
        Pk_location.objects.bulk_update(update_list, ['empty'])


def adjacent_priority_algorithm(result, num):
    try:
        # 전체 주차 공간 불러 오기
        parking_area = Pk_location.objects.filter(building_num=num)

        update_list = []

        # label[0] : x, label[1] : y, label[2] : w, label[3] : h
        for label in result:
            lx, ly, lw, lh = label[0], label[1], label[2], label[3]

            lx_min = lx - lw/2
            lx_max = lx + lw/2
            ly_min = ly - lh/2
            ly_max = ly + lh/2

            include = []

            # 라벨 안에 포함 되는 주차 구역 구하기
            for pk in parking_area:
                px, py, pw, ph = pk.x, pk.y, pk.w, pk.h
                points = [[px+pw/2, py], [px-pw/2, py], [pw, py+ph/2], [pw, py-ph/2]]

                for point in points:
                    if lx_min < point[0] < lx_max and ly_min < point[1] < ly_max:
                        include.append(pk)
                        break

            # 포함 되는 주차 구역 중에서 라벨의 밑변과 가장 가까운 구역 찾기 -> y 좌표 이요
            min_distance = float("inf")
            result = None
            for pk in include:
                y_min = pk.y - pk.h/2
                distance = math.abs(ly_min - y_min)

                if distance < min_distance:
                    min_distance = distance
                    result = pk

            # 최종 결과값 넣기
            result.empty = False
            update_list.append(result)

        Pk_location.objects.bulk_update(update_list, ['empty'])

    except ObjectDoesNotExist:
        raise "Object Not Exist"


def change_file(parking_name):
    # occupied 만 존재 하도록 파일을 변경

    dir_path = 'YOLO/yolov5/runs/detect/' + parking_name + "/labels"

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
