# up down game
import random

# 정답 숫자 랜덤으로 준비
answer = random.randint(1, 50)

while True:
    # 유저 입력 넣기 , 형변환
    x = int(input("1 ~ 50 사이의 숫자를 입력하세요"))

    # 입력값 검증
    if not(1 <= x <= 50):
        print("wrong number !")
        continue

    # 결과 출력
    if answer > x:
        print("UP")
    elif answer < x:
        print("DOWN")
    else:
        print("correct !")
        break