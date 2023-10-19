import random
import path

try:
    # 텍스트 파일의 경로 불러오기
    dir_path = path.get_path()

    # 텍스트 파일 열고 단어 불러오기(리스트로 저장)
    f = open(dir_path, 'r')
    lines = tuple(f.readlines())

# 텍스트 파일의 경로 오류가 난 경우 프로그램 종료
except TypeError or FileNotFoundError:
    print(dir_path)
    print('파일 경로 오류')
    exit()

# 경로 오류 없으면 정상 작동
else:
    # 단어 중복을 방지하기 위한 세트 생성
    num_list = set()

    # 랜덤으로 단어 가져오는 함수
    def get_text():
        while True:
            # 숫자 랜덤 생성
            num = random.randint(0,998)
            # 중복 단어 확인
            if num not in num_list:
                num_list.add(num)
                break
            
        # 랜덤 숫자에 따른 단어 저장
        text = lines[num]

        # 단어를 읽어올때 끝에 붙어있는 '\n' 제거
        if num == 998:
            return text
        else:
            return text[:-1]
