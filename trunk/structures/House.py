class House(object):
    cells = []
    overlappingHouses = []
    
    def __init__(self, cellList):
        for i in cellList:
            self.cells.append(i)
            i.addHouse(self)
    
    def addHouse(house1, house2):
        house1.overlappingHouses.append(house2)
        house2.overlappingHouses.append(house1)
    
    