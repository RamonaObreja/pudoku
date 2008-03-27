class Cell(object):
    horizontal = 0
    vertical = 0
    value = []
    maxValue = 0
    immutable = False
    houses = []
    
    def __init__(self, hor, vert, max):
        '''Constructor for a Cell that is not a given'''
        self.horizontal = hor
        self.vertical = vert
        self.maxValue = max
        self.value = range(1,max+1)
    
    def addHouse(self, house):
        self.houses.append(house)

class EmptyCell(Cell):
    def __init__(self, hor, vert):
        '''Constructor for a Cell that should remain empty'''
        self.horizontal = hor
        self.vertical = vert
        self.maxValue = -1
        self.immutable = True

class GivenCell(Cell):
    def __init__(self, hor, vert, max, val):
        '''Constructor for a Cell that is a given'''
        self.horizontal = hor
        self.vertical = vert
        self.maxValue = max
        self.value = []
        self.value.append(val)
        self.immutable = True
        