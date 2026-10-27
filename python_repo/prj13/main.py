# 클래스 , 객체 만들기 위함
# 객체 : data + function

class Book:
    def __init__(self):
        self.a = 10
        self.b = 20

    def f01(self):
        print("f01 called")

    def f02(self):
        print("f02 called")

    def f03(self):
        print("f03 called")


book = Book() # 클래스명() = 해당 클래스를 바탕으로 객체 생성
book.f01()  # book 안 쪽에 있는 book을 실행하기 위해 book.f01()
book.f02()
book.f03()
print(book.a)
print(book.b)
