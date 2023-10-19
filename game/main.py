import textfile
import small_game

while True:
    answer = textfile.get_text()    # 랜덤 단어 저장
    life = 6                        # 목숨 개수
    text = '-' * len(answer)        # 보여지는 텍스트
    duplicate = []                  # 중복 앒파벳 저장 리스트
    none = set()                    # 틀린 알파벳 저장 세트

    # 게임(라운드) 시작
    small_game.word(answer, life, none, text, duplicate)
    
    # 다른 단어로 게임 계속할지 입력
    if small_game.gostop():
        print("이용해주셔서 감사합니다.")
        break
    