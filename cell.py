
class Cell():
    def __init__(self,character):
        self.character=character
        if character == '#':
            self.walkable=False
            self.cost=-1
        elif character== '~':
            self.walkable=True
            self.cost=800
        elif character== '*':
            self.walkable=True
            self.cost=200
        elif character== '+':
            self.walkable=True
            self.cost=150
        elif character== 'X':
            self.walkable=True
            self.cost=120
        elif character== '_':
            self.walkable=True
            self.cost=100
        elif character== 'H':
            self.walkable=True
            self.cost=70
        elif character== 'T':
            self.walkable=True
            self.cost=50


