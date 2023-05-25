from django.shortcuts import render
from django.http import JsonResponse
import requests
import datetime
import os
import cv2

# Create your views here.

# CCTV 영상 저장소에서 특정 주차장의 현재 날짜의 영상을 불러오는 기능
def get_today_parking_video(parking_name):
    today = datetime.date.today()
    today_directory = os.path.join('/path/to/video/directory', str(today))
    video_directory = os.path.join(today_directory, parking_name)
    # os.listdir 로 해당 디렉토리의 파일들을 가져와, key 를 os.path.getctime 로 설정하여 파일들 중 최신 파일을 선택하여 반환
    latest_video_file = max(os.listdir(video_directory), key=os.path.getctime)
    video_path = os.path.join(video_directory, latest_video_file)

    return video_path

# 불러온 영상에서 사진을 캡쳐하는 기능 -> 라즈베리파이에서 수행
def capture_latest_frame(video_path):
    # 동영상 파일 열기
    cap = cv2.VideoCapture(video_path)
    # 총 프레임 수 구하기
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
    # 마지막 프레임의 인덱스로 이동
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count - 1)
    # 해당 프레임의 이미지 가져오기
    # ret = 프레임을 성공적으로 읽었는지 여부를 반환하는 boolean 값
    ret, frame = cap.read()

    # 가져온 이미지를 다음 경로에 저장
    if ret:
        #cv2.imwrite('/path/to/image/directory/latest_frame.jpg', frame)
        cv2.imwrite('/Users/jieon/temp/latest_frame.jpg', frame)

    # 동영상 파일 닫기
    cap.release()
    image_path = '/Users/jieon/temp/latest_frame.jpg'
    return image_path


# 캡쳐한 사진을 주차장 별로 저장하는 기능
def save_parking_image(building_num):
    image_path = os.path.join('YOLO_nodel/yolov5/data/images/', building_num)
    latest_frame_path = '/latest_frame.jpg'
    os.rename(latest_frame_path, image_path)

# 캡쳐된 사진을 삭제하는 기능
def delete_parking_image(parking_name):
    image_path = os.path.join('/path/to/image/directory', parking_name + '.jpg')
    os.remove(image_path)

# 주차장 별로 마지막으로 캡쳐한 시간을 저장 및 갱신하는 기능
def update_last_captured_time(parking_name):
    # 주차장에 대한 텍스트 파일을 만들고 텍스트 파일에 현재의 시간을 작성
    last_captured_time_path = os.path.join('/path/to/last/captured/time/directory', parking_name + '.txt')
    with open(last_captured_time_path, 'w') as f:
        f.write(str(datetime.datetime.now()))

# 가장 최근에 캡쳐된 사진을 조회하는 기능
def get_latest_parking_image(parking_name):
    image_path = os.path.join('/path/to/image/directory', parking_name + '.jpg')
    return image_path

# 캡쳐한 사진을 resize 하는 기능
def resize_image(image_path, building_num):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    # interpolation : 리사이징에 사용할 알고리즘
    resized = cv2.resize(img, (1280, 1280), interpolation=cv2.INTER_AREA)
    cv2.imwrite(f'YOLO_model/yolov5/data/images/{building_num}/resized_image.jpg', resized)


# 캡쳐된 사진을 모델로 전송하는 기능
def get_resized_parking_image(parking_name):
    image_path = os.path.join('/Users/jieon/temp', parking_name + '.jpg')
    resized_image_path = os.path.join('/Users/jieon/temp', parking_name + '_resized.jpg')
    resized_image = resize_image(image_path)
    cv2.imwrite(resized_image_path, resized_image)
    return resized_image


# 터미널 명령어를 이용해 detect.py 실행
def execute_detect_py(building_num):
    # detect.py 가 있는 폴더 경로
    dir_path = 'YOLO_model/yolov5'

    terminal_command = f"cd {dir_path}"
    os.system(terminal_command)

    terminal_command = f"python3 detect.py --weights runs/train/weights/best.pt --img 1280 --conf 0.4 "\
                       f"--source data/images/{building_num} --save-txt  --name {building_num}/result"
    os.system(terminal_command)


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
