from cctv import views
from building.models import Building, Pk_location
from pklot.serializers import buildingSerializers, locationSerializers
from django.core.exceptions import ObjectDoesNotExist

"""예외 처리 필요"""


def get_sector(sector_id):
    try:
        buildings = Building.objects.filter(sector=sector_id)
        serializer = buildingSerializers(buildings, many=True)
        return serializer.data
    except ObjectDoesNotExist:
        raise "Object Not Exist"


def get_subsector(sector_id, subsector_id):
    try:
        locations = Pk_location.objects.select_related('building').filter(where=["sector = '%d'", "sub_sector = '%s'"],
                                                                          params=[sector_id, subsector_id])
        serializer = locationSerializers(locations, many=True)
        return serializer.data
    except ObjectDoesNotExist:
        raise "Object Not Exist"


def update_pklocation(result, num):
    try:
        location_set = Pk_location.objects.filter(building_num=num)
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
    except ObjectDoesNotExist:
        raise "Object Not Exist"
