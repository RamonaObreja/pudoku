class Grid(object):
    cells = []
    houses = []
    
    def __init__(self, cellList, houseList):
        self.cells = cellList
        self.houses = houseList
    
    def getCell(self, hor, vert):
        def __cellMatches(cell):
            return cell.horizontal == hor and cell.vertical == vert
        return filter(__cellMatches, cells)
    
    def getHouses(self, hor, vert):
        def __houseMatches(house):
            goodCell = False
            for i in house.cells:
                if(i.horizontal == hor and i.vertical == vert):
                    goodCell = True
            return goodCell
        return filter(__houseMatches, houses)
    
    def __str__(self):
        return 'stub'