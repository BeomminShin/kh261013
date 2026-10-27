# 서브웨이 (빵, 야채 -> 총 금액)

print("===== 서브웨이 키오스크=====")
print("----- 빵을 1개 고르고, 야채를 자유롭게 추가하세요")

# 빵 메뉴판
print("\n-----빵 선택-----\n")
print("1. 플랫 브레드 (1000원)")
print("2. 호밀빵 (2000원)")
print("3. 식빵 (3000원)")
# 빵 선택 , 선택과 동시에 금액 업데이트
bread_num = input("빵 번호 : ")
if bread_num == "1":
    price = 1000
elif bread_num == "2":
    price = 2000
elif bread_num == "3":
    price = 3000

while True:
    # 야채 메뉴판
    print("\n-----야채 선택-----\n")
    print("0 야채 선택 종료")
    print("1 올리브 (100원)")
    print("2 오이 (200원)")
    print("3 당근 (300원)")
    print("4 양배추 (400원)")
    print("5 양상추 (500원)")

    # 야채 선택 , 선택과 동시에 금액 업데이트
    veg_num = input("야채 번호 : ")
    if veg_num == "1":
        price = price + 100
    elif veg_num == "2":
        price = price + 200
    elif veg_num == "3":
        price = price + 300
    elif veg_num == "4":
        price = price + 400
    elif veg_num == "5":
        price = price + 500
    elif veg_num == "0":
        break

# 금액
print(f" 결제하실 금액은 {price}원 입니다.")