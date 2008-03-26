class Cell(object):
    horizontal = 0
    vertical = 0
    value = []
    maxValue = 0
    given = False
    houses = []
    
    def __init__(self, hor, vert, max):
        '''Constructor for a Cell that is not a given'''
        self.horizontal = hor
        self.vertical = vert
        self.maxValue = max
        for i in range(1,max+1):
            self.value.append(i)
    
    def addHouse(self, house):
        self.houses.append(house)

class EmptyCell(Cell):
    def __init__(self, hor, vert):
        '''Constructor for a Cell that should remain empty'''
        self.horizontal = hor
        self.vertical = vert
        self.maxValue = -1

class GivenCell(Cell):
    def __init__(self, hor, vert, max, val):
        '''Constructor for a Cell that is a given'''
        self.horizontal = hor
        self.vertical = vert
        self.maxValue = max
        self.given = True
        self.value.append(val)