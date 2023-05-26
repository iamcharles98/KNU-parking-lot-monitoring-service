from django.http import Http404

# from cctv import views
from building.models import Building, Pk_location
from pklot.serializers import buildingSerializers, locationSerializers
from django.core.exceptions import ObjectDoesNotExist

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
    if location_set.count() == 0:
        return Http404("Building_num is Wrong")
    else:
        update_list = []
        for location in location_set:
            Xmin = location.x - location.w // 2
            Xmax = location.x + location.w // 2
            Ymin = location.y - location.h // 2
            Ymax = location.y + location.h // 2
            for el in result:
                x, y = el[0], el[1]
                if Xmin <= x <= Xmax and Ymin <= y <= Ymax:
                    location.empty = False
                    update_list.append(location)
        Pk_location.objects.bulk_update(update_list, ['empty'])
