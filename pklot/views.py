import datetime

from django.http import *
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from building.models import Building, Pk_location
from pklot.serializers import buildingSerializers, locationSerializers


# Create your views here.
# sub_sector 별 주차공간 보내기
def get_sector(request):
    if request.method == 'GET':
        sector_id = request.GET['sector_id']
        try:
            buildings = Building.objects.filter(sector=sector_id)
        except Building.DoesNotExist:
            raise "Not Exist"
        finally:
            serializer = buildingSerializers(buildings, many=True)
            print(serializer.data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def get_subsector(request):
    if request.method == 'GET':
        sector_id = request.GET['sector_id']
        subsector_id = request.GET['subsector_id']
        try:
            locations = Pk_location.objects.select_related('building').filter(
                where=["sector = '%d'", "sub_sector = '%s'"], params=[sector_id, subsector_id])
            serializer = locationSerializers(locations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK, content_type=JsonResponse)
        except Pk_location.DoesNotExist:
            return Response("Not Exist Location", status=status.HTTP_404_NOT_FOUND)
