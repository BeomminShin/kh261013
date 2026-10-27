from practice.animal import Animal
from practice.athtele import Athlete
from practice.battleGrounds import Gun
from practice.food import Food
from practice.pokemon import Pokemon

print("객체 만들기~~")

# 빨간 줄이 그어져있을 때 마우스커서 올리고 alt + enter
# x = Animal("피카츄", 50, "전기타입")
# print(x.name)
# print(x.weight)
# print(x.type)
# print(type(x))
#
# y = Animal("갸라도스", 300, "물속성")
# print(y.name)
# print(y.weight)
# print(y.type)
# print(type(y))
#
# z = Animal(n="롱스톤", w=800, t="땅속성")
# print(z.name)
# print(z.weight)
# print(z.type)
# print(type(z))

# p1 = Pokemon("피카츄", 100)
# p2 = Pokemon("파이리", 90)
# p3 = Pokemon("꼬부기", 80)
#
# print(p1)
# print(p2)
# print(p3)

# x = Food(name="제육볶음" , price=9000)
# print(x)
#
# g = Gun(name="ACE 32", category="AR")
# print(g)

# x = Athlete(name= "호날두" , height=187, weight=85)
# print(x)
# x.eat()

x = Athlete(name= "호날두" , height=187, weight=85)
print(x)
x.eat()