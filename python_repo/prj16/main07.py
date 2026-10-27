# method override

class Drink:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("<Drink> self.name : " , self.name)

class Coffee(Drink):
    def print_info(self):
        print("<Coffee> self.name : " , self.name)
# 기본적으로 Drink 안에 있는 메서드를 가져다 씀
d = Drink("딸기스무디")
c = Coffee("라떼")

d.print_info()
c.print_info()
