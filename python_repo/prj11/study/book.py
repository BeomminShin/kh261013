print("도서 관리 프로그램")

book_list = []
def print_menu():
    print("0. 종료하기")
    print("1. 도서 등록")
    print("2. 도서 목록 조회")
    print("3. 도서 상세 조회")
    print("4. 도서 수정하기")
    print("5. 도서 삭제하기")

def insert_book():
    print("-----도서 등록-----")
    t = input("도서 제목 : ")
    p = input("도서 가격 : ")
    d = {
        "책 제목" : t,
        "가격" : p,
    }
    book_list.append(d)
    print(f"도서 등록 완료 ! {t} / {p}")

def select_book_list():
    print("-----도서 목록 조회-----")
    for d in book_list:
        print(f"{d['책 제목']} / {d['가격']}")

def select_book_one():
    print("-----도서 상세 조회-----")

def update_book():
    print("-----도서 정보 수정-----")

def delete_book():
    print("-----도서 정보 삭제-----")

while True:
    print_menu()
    n = int(input("메뉴 번호 : "))
    match n:
        case 1:
            insert_book()
        case 2:
            select_book_list()
        case 3:
            select_book_one()
        case 4:
            update_book()
        case 5:
            delete_book()
        case _:
            print("올바른 메뉴 번호를 입력하세요")