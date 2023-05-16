from rest_framework import serializers
from building.models import Building, Pk_location


class buildingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('building_name',  'pk_count',  'sub_sector')

class locationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pk_location
        fields = ('building_num', 'pk_area', 'empty')
