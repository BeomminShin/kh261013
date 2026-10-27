# 함수 형태
# def 함수이름(매개변수):
#     실행 할 코드
#     실행 할 코드
#     실행 할 코드
#     return 값

# 매개변수(parameter) 없음 , 반환 값(return) 없음
# def hello():
#     print("hello")
#     print("world")
#     print(1+2+3+4+5)
#     print(True)
# hello()

# 매개변수(parameter) 있음 , 반환 값(return) 없음
# def hello(x):
#     print(f"{x}님 Welcome ~")
# hello("GG")
#
# def print_plus_result(a, b):
#     result = a + b
#     print(result)
#
# print_plus_result(3,4 )
# 매개변수(parameter) 없음 , 반환 값(return) 있음
# def get_number():
#     return 10

# x= get_number()
# print(x)
# 매개변수(parameter) 있음 , 반환 값(return) 있음
def plus_ten(x):
    result = x + 10
    return result

a = plus_ten(3)
print(a)
