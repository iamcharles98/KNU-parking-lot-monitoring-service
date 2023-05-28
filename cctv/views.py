from django.shortcuts import render
from django.http import JsonResponse
import requests
import datetime
import os
import shutil
from PIL import Image
from django.http import HttpResponse


# Create your views here.
# 이미지를 1280*1280의 크기로 resize
def resize_image(building_num):
    building_num_str = str(building_num)
    directory_path = os.path.join('YOLO_model/yolov5/data/images/', building_num_str)
    image_path = os.path.join(directory_path, f'{building_num}.jpeg')
    target_size = (1280, 1280)

    try:
        # Open the image file
        image = Image.open(image_path)

        # Resize the image
        resized_image = image.resize(target_size)

        # Save the resized image, overwriting the original file
        resized_image.save(image_path)

        print(f"Image '{image_path}' resized and overwritten successfully.")
    except IOError:
        print(f"Unable to open or resize image: {image_path}")


# 터미널 명령어를 이용해 detect.py 실행
def execute_detect_py(building_num):
    # 결과를 생성하기 전에 기본의 디렉토리와 파일 삭제
    delete_directory(1, building_num)

    # image 를 detection 하기 전에 resize 하기
    resize_image(building_num)

    terminal_command = f"python3 YOLO_model/yolov5/detect.py --weights YOLO_model/yolov5/runs/train/weights/best.pt --img 1280 --conf 0.4 "\
                       f"--source YOLO_model/yolov5/data/images/{building_num} --save-txt  --name {building_num}/result"
    os.system(terminal_command)

    return HttpResponse("run!")

# 결과 가져 오기
def get_result(parking_name):
    # txt 파일이 있는 경로로 들어가기
    dir_path = 'YOLO/yolov5/runs/detect/' + parking_name + "/labels"

    try:
        files = sorted(os.listdir(dir_path))
        if len(files) > 0:
            latest_file = files[len(files) - 1]
            file_path = os.path.join(dir_path, latest_file)

            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    value = line.split()

                    # txt 파일 내용 분류
                    if len(value) == 5:
                        check = int(value[0])
                        x = float(value[1])
                        y = float(value[2])
                        w = float(value[3])
                        h = float(value[4])
                    else:
                        print("Invalid line format : ", line)

    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An error occurred while reading the file.")


# detection 전에 이전 디렉토리 삭제하기

def delete_directory(cand, building_num):
    building_num_str = str(building_num)
    # detection을 할 디렉토리 삭제
    if cand == 0:
        directory_path = os.path.join('YOLO_model/yolov5/data/images/', building_num_str)
    # detection 결과를 저장한 디렉토리 삭제
    else:
        directory_path = os.path.join('YOLO_model/yolov5/runs/detect/', building_num_str)

    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' successfully deleted.")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to delete directory '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred while deleting directory '{directory_path}': {str(e)}")
