from building.models import Building, Pk_location
from pklot.serializers import buildingSerializers, locationSerializers


def get_sector(sector_id):
    try:
        buildings = Building.objects.filter(sector=sector_id)
    except Building.DoesNotExist:
        raise "Not Exist"
    finally:
        serializer = buildingSerializers(buildings, many=True)
        return serializer.data


def get_subsector(sector_id, subsector_id):
    try:
        locations = Pk_location.objects.select_related('building').filter(where=["sector = '%d'", "sub_sector = '%s'"],
                                                                          params=[sector_id, subsector_id])
        serializer = locationSerializers(locations, many=True)
    except Pk_location.DoesNotExist:
        raise "Not Exist"
    finally:
        return serializer.data
