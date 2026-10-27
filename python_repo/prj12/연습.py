# 1. 숫자 맞히기 2. 가위바위보

import random
from unittest import case

correct = random.randint (1,50)
correct_01 = random.randint (1,3)
def game_menu():
    print("0. 프로그램 종료")
    print("1. 숫자 맞히기 게임")
    print("2. 가위바위보")
def number_game():
    while True:
        x = int(input("1~50 사이 숫자를 입력하세요"))
        if correct > x:
            print("UP")
        elif correct < x:
            print("DOWN")
        else:
            print("---correct---")
            break

def rsp_game_01(num):
    match num:

    return num

def rsp_game():
    while True:
        print("1. 가위 2. 바위 3. 보 선택해서 입력해주세요")
        a = int(input("선택 : "))
        d = {
            1 : "가위",
            2 : "바위",
            3 : "보",
        }
        match a:
            case 1:

            case 2:
                pass
            case 3:
                pass



while True:
    game_menu()
    n = int(input("게임 번호를 입력해주세요 : "))
    match n:
        case 0:
            print("프로그램을 종료합니다")
            break
        case 1:
            number_game()
        case 2:
            rsp_game()
        case _:
            print("잘못 입력하였습니다.")

