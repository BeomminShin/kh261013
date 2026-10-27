class Athlete():
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return (f" 선수명 : {self.name} 키 :{self.height} 몸무게 : {self.weight}")

    def eat(self):
        print("밥먹는중")
