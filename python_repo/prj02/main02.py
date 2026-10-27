# 문자열(string) 표기 방법 : 쌍따옴표 1개, 3개 , 작은따옴표 1개
# f-string : {변수} 로 변수 처리 가능, 변수는 숫자로 적기 불가능
user_name = "신범민"
a= 27
b= 177
c= 72
print(user_name)
print(f"안녕하세요 저는 {user_name} 입니다")
print(f"저 {user_name}의 나이는 {a} 살이고")
print(f"저 {user_name}의 {b}키는 이며")
print(f"저 {user_name}의 몸무게는{c} 입니다")