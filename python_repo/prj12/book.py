# 종료하기
# 도서 등록
# 도서 조회
# from unittest import case

book_list = []


def print_menu():
    print("===== BOOK =====")
    print("0. exit")
    print("1. insert")
    print("2. select")


def insert_book():
    print("-----insert book-----")
    t = input("title : ")
    c = input("content : ")
    d = {
        "title": t,
        "price": c,
    }
    book_list.append(d)
    print("inselt finish")


def select_book():
    print("-----select book-----")
    for d in book_list:
        print(f"{d['title']} / {d['price']}")


while True:
    print_menu()
    n = int(input())
    match n:
        case 0:
            print("종료하겠습니다")
            break  # ; = 명령 1개 끝남
        case 1:
            insert_book()
        case 2:
            select_book()
