# 나이 입력받고 연령대 출력하기
# 10대, 20대, 30대, 40대, 기타
#

age = input("당신의 나이는?")
age = int(age)
if age < 0:
    print("그런 나이는 존재하지 않아요")
elif age < 10:
    print("어린이")
elif 10 <= age < 20:
    print("10대")
elif age < 30:
    print("20대")
elif age < 40:
    print("30대")
elif age < 50:
    print("40대")
else:
    print("기타")

