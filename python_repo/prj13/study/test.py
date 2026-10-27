# study.person에 Person을 불러온다
from study.person import Person

# 모둘 전체 가져오기
# 접근방법 : 모듈명.이름
# import study.person

# study.person.Person()
# study.person.f01()
# print(study.person.x)

# 특정 요소만 가져오기
# from person import y , f03
#
# 기존 파일에 있던 거랑 이름이 같아 충돌이 될 경우 아래와 같이 변경 가능
# from person import f01 as f04

x = Person("hong",20)
y = Person("kim",30)
z = Person("lee",40)
print(x.name)
print(x.age)