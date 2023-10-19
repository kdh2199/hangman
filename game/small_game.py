import os
import setting
import time

# 운영체제에 따른 화면 초기화 설정
clear = setting.clear_os()
# 대기 시간
wait = 1

# 현재 상태 출력
def state(hp, wrong, now):
    print("현재 남은 시도 횟수 : {0}\n틀린 알파벳 : {1}\n{2}\n".format(hp, wrong, now))

# 단어 한개로 반복하여 알파벳 맞추기
def word(answer, life, none, text, duplicate):
    while True:
        os.system(clear)
        state(life, '' if len(none)==0 else none, text)
        alphabet = input("알파벳을 입력하세요 (강제종료 : exit) : ").lower()
        num = answer.find(alphabet)

        if alphabet == 'exit':
            print("해당 라운드를 강제 종료합니다.")
            break
        elif alphabet < 'A' or (alphabet > 'Z' and alphabet < 'a') or alphabet > 'z':
            print("알파벳이 아닙니다.")
            time.sleep(wait)
        elif len(alphabet) > 1:
            print("알파벳 한개만 입력해주세요.")
            time.sleep(wait)
        elif alphabet in duplicate:
            print("중복된 알파벳")
            time.sleep(wait)
        elif alphabet in none:
            print("이미 틀린 알파벳입니다.")
            time.sleep(wait)
        elif num == -1:
            print("없는 알파벳")
            none.add(alphabet)
            life -= 1
            time.sleep(wait)
        else:
            duplicate.append(alphabet)
            while num != -1:
                text = ''.join(text[:num] + answer[num] + text[num + 1:])
                num = answer.find(alphabet, num + 1)

        # 목숨이 0이거나 정답을 맞추면 종료
        if life == 0:
            os.system(clear)
            print("Game Over\n정답 : " + answer)
            break
        if text == answer:
            print("정답입니다!!")
            break

# 다른 단어로 게임 계속 할지 입력
def gostop():
    while True:
        yesorno = input("게임을 계속 하시겠습니까? (y/n) : ")
        if yesorno == 'N' or yesorno == 'n':
            return True
        elif yesorno == 'Y' or yesorno == 'y':
            return False
        else:
            print("다시 입력해주세요.")
