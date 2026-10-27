class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"음식 이름 : {self.name}, 음식 가격 = {self.price}"
