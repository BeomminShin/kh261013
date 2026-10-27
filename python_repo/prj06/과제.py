print("=== 카페 키오스크 프로그램 ===")

price = 0

while True:
  print("\n--- [메뉴판] ---")
  print("1. 아메리카노 (3000원)")
  print("2. 카페라떼 (4000원)")
  print("3. 카푸치노 (4000원)")
  print("4. 결제 및 종료")

  choice = input("원하는 메뉴 번호를 입력하세요: ")

  if choice == "1":
    price += 3000
    print("아메리카노가 장바구니에 담겼습니다. (+3000원)")

  elif choice == "2":
    price += 4000
    print("카페라떼가 장바구니에 담겼습니다. (+4000원)")

  elif choice == "3":
    price += 4000
    print("카푸치노가 장바구니에 담겼습니다. (+4000원)")

  elif choice == "4":
    print(f"\n 총 결제 금액은 **{price}원**입니다.")
    print("이용해 주셔서 감사합니다. 안녕히 가세요!")
    break

  else:
    print("잘못된 번호입니다. 1부터 4 사이의 숫자를 다시 입력해 주세요.")