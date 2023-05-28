from django.shortcuts import render
from pklot import utils
from django.http import HttpResponse

# Create your views here.
def test(requests):
    result_path = '/Users/jieon/Desktop/KNU_Project/YOLO_model/yolov5/runs/detect/415/result/labels/415.txt'
    utils.change_file(415)

    utils.update_pklocation(utils.read_rows_from_file(result_path), 415)

    return HttpResponse("test")

def test2(requests):
    result_path = '/Users/jieon/Desktop/KNU_Project/temp2.txt'
    utils.change_file(416)

    utils.adjacent_priority_algorithm(utils.read_rows_from_file(result_path), 416)

    return HttpResponse("test2")
