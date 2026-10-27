# 도서관리 프로그램

class Book:
    def __init__(self, a, b):
        self.title = a
        self.price = b

book_list = []

def print_menu():
    print("0. 종료")
    print("1. 도서 등록")
    print("2. 목록 조회")


def insert():
    t = input("제목 : ")
    p = input("가격 : ")
    x = Book(t, p)
    book_list.append(x)


def select():
    for x in book_list:
        print(f"{x.title} / {x.price}")


while True:
    print_menu()
    n = int(input("번호를 입력해주세요 : "))
    match n:
        case 0:
            print("프로그램을 종료합니다")
            break
        case 1:
            insert()
            print("등록이 완료돼었습니다")
        case 2:
            print("목록을 조회합니다")
            select()
        case _:
            print("잘못 입력하셨습니다")