# 게임 정답 단어
answer = ('apartment', 'bear', 'cat')
# 게임 시작/정지 변수
game = True

# 현재 상태 출력 함수
def state(hp, wrong, now):
    print("현재 남은 시도 횟수 : {0}\n틀린 알파벳 : {1}\n{2}\n".format(hp, wrong, now))

# 게임 시작
for i in answer:
    stop = False            # stop : 전체 게임 종료 변수
    life = 6                # life : 틀릴 수 있는 횟수
    length = len(i)         # length : 단어의 길이
    text = '-' * length     # text : 단어의 개수만큼 '-'로 출력, 맞춘 알파벳은 공개
    duplicate = []          # duplicate : 중복입력한 알파벳
    none = []               # none : 단어에 포함되지 않은 알파벳

    while game:
        # 현재 상태 출력
        state(life, none, text)
        alphabet = input("알파벳을 입력하세요 : ")
        # 알파벳이 정답에 포함되었는지 확인
        num = i.find(alphabet)

        # 입력받은 알파벳이 정답에 없으면 목숨 -1
        if num == -1:
            print("없는 알파벳")
            if alphabet not in none:
                none.append(alphabet)
                life -= 1
        # 이미 입력받을 알파벳 입력시 목숨 -1
        elif alphabet in duplicate:
            print("중복된 알파벳")
            life -= 1
        # 알파벳이 답에 있을경우 문자열 수정
        else:
            duplicate.append(alphabet)
            while num != -1:
                text = ''.join(text[:num] + i[num] + text[num + 1:])
                num = i.find(alphabet, num + 1)

        # 목숨이 0이 되면 해당 라운드 종료
        if life == 0:
            print("Game Over\n정답 : " + i)
            game = False
        # 정답을 맞추면 해당 라운드 종료
        if text == i:
            print("정답입니다!!")
            game = False

    # 다른 단어로 게임을 계속할지 입력
    while True:
        yesorno = input("게임을 계속 하시겠습니까? (y/n) : ")
        if yesorno == 'N' or yesorno == 'n':
            stop = True
            break
        elif yesorno == 'Y' or yesorno == 'y':
            game = True
            break
        else:
            print("다시 입력해주세요.")
    if stop:
        print("게임을 종료합니다.")
        break
