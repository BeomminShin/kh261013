# 도서관리

book_list = []

def insert_book():
    print("---- 도서 정보 입력----")
    t = input("title : ")
    p = input("price : ")
    x = {
        "title": t,
        "price": p
    }
    book_list.append(x)


def select_book_list():
    print("----- 도서 정보 등록 -----")
    print("제목 / 가격")
    for d in book_list:
        print(f"{d["title"]} / {d["price"]}")


while True:
    print("1. 도서 등록")
    print("2. 도서 조회")

    menu = int(input("menu : "))
    match menu:
        case 0:
            break
        case 1:
            insert_book()
        case 2:
            select_book_list()
