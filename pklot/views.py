from django.shortcuts import render
from pklot import utils
from django.http import HttpResponse

# Create your views here.
def test(requests):
    utils.update_pklocation(utils.read_rows_from_file('/Users/jieon/Desktop/KNU_Project/temp.txt'), 417)
    return HttpResponse("test")

def test2(requests):
    utils.adjacent_priority_algorithm(utils.read_rows_from_file('/Users/jieon/Desktop/KNU_Project/temp2.txt'), 416)
    return HttpResponse("test2")

def run(requests):

    return HttpResponse("Run YOLO model")