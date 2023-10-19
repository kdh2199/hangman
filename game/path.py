import os

def get_path():
    now_path = os.getcwd()
    file_list = os.listdir(now_path)

    if 'text.txt' in file_list:
        path = './text.txt'
    elif 'game' in file_list:
        path = './game/text.txt'
    elif 'hangman-main' in file_list:
        path = './hangman-main/game/text.txt'
    else:
        path = now_path , file_list
    
    return path
