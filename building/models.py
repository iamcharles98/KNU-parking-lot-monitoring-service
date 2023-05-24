from django.db import models

# Create your models here.
class Building(models.Model):
    id = models.AutoField(primary_key=True)
    building_num = models.IntegerField(unique=True, verbose_name='건물 번호')
    building_name = models.CharField(max_length=20, verbose_name='건물 이름')
    pk_size = models.IntegerField(verbose_name='건물의 총 주차 공간 개수')
    pk_count = models.IntegerField(verbose_name='건물의 주차 가능한 공간의 개수')
    modifiedAt = models.DateTimeField(auto_now=True, verbose_name='최근 수정 시간')
    sector = models.IntegerField(verbose_name='빌딩이 속한 섹터', null=True)
    sub_sector = models.CharField(max_length=2, verbose_name='빌딩이 속한 서브 섹터', null=True)

    class Meta:
        db_table = 'building'
        verbose_name = '경북대학교 건물'
        verbose_name_plural = '경북대학교 건물'

class Pk_location(models.Model):
    building_num = models.ForeignKey(Building, to_field='building_num', db_column='building_num', on_delete=models.CASCADE)
    pk_area = models.IntegerField(verbose_name='건물에서 주차공간의 번호')
    x = models.FloatField(verbose_name='주차공간의 x 좌표')
    y = models.FloatField(verbose_name='주차공간의 y 좌표')
    w = models.FloatField(verbose_name='주차공간의 너비')
    h = models.FloatField(verbose_name='주차공간의 높이')
    empty = models.BooleanField(verbose_name='주차공간 사용가능 여부')

    class Meta:
        db_table = 'pk_location'
        verbose_name = '각 건물의 주차 공간'
        verbose_name_plural = '각 건물의 주차 공간'