class Champion:
    def __init__(self, name, position, line):
        self.name = name
        self.position = position
        self.line = line
    def __str__(self):
        return (f" champion : {self.name}, position : {self.position} , line : {self.line}")