class Gun:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    def __str__(self):
        return (f"총 이름 : {self.name}, 분류 : {self.category}")