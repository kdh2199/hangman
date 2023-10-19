import platform

# 실행 시스템 운영체제 확인
def clear_os():
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
        clear = 'clear'
    elif platform.system() == 'Windows':
        clear = 'cls'
    return clear