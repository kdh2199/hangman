import os

# 텍스트 파일의 경로를 받아오는 함수
def get_path():
    # 현재 작업 폴더 경로
    now_path = os.getcwd()
    # 현재 작업 폴더 안에 있는 파일 리스트
    file_list = os.listdir(now_path)

    # 텍스트 파일이 현재 작업 폴더에 들어있는 경우 경로 설정
    if 'text.txt' in file_list:
        path = './text.txt'
    # 현재 작업 폴더에 'game' 폴더가 있는 경우 (텍스트 파일이 'game' 폴더 안에 들어있는 경우) 경로 설정
    elif 'game' in file_list:
        path = './game/text.txt'
    # 현재 작업 폴더에 'hangman-main' 폴더가 있는 경우 (텍스트 파일이 'hangman-main' 폴더 안에 들어있는 경우) 경로 설정
    elif 'hangman-main' in file_list:
        path = './hangman-main/game/text.txt'
    # 이외에 텍스트 파일이나 폴더를 찾을 수 없는 경우 현재 작업 폴더 경로 반환
    else:
        path = now_path , file_list
    
    return path
