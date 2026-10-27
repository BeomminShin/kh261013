class Job:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return (f" 직업 이름 : {self.name}, 직업 분류 : {self.category}")