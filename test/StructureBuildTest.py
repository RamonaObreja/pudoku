import structures.Cell
import structures.House
import structures.Grid
import solver.Solver

def tryConstruct():
    maxValue = 9
    cells = []
    houses = []
    print 'Starting Cell creation'
    #Add first row
    for i in range(0, 9):
        cells.append(structures.Cell.Cell(i,0,maxValue))
    #Add second row
    for i in range(0, 9):
        cells.append(structures.Cell.GivenCell(i,1,maxValue,i+1))
    #Add other rows
    for i in range(2, 9):
        for j in range(0, 9):
            cells.append(structures.Cell.Cell(j,i,maxValue))
    print 'Cells created'
    print 'Cell test started'
    for i in cells:
        print str(i.horizontal) + " " + str(i.vertical) + " " + str(i.value)
    print 'Cell test finished'
    
    print 'Starting House Creation'
    #Rows
    for i in range(0,9):
        def __cellMatches(cell):
            return cell.vertical == i
        houses.append(structures.House.House(filter(__cellMatches,cells)))
    #Columns
    for i in range(0,9):
        def __cellMatches(cell):
            return cell.horizontal == i
        houses.append(structures.House.House(filter(__cellMatches,cells)))
    #3x3 square
    for i in range(0,3):
        for j in range(0,3):
            def __cellMatches(cell):
                return cell.horizontal/3 == i and cell.vertical/3 == j
            houses.append(structures.House.House(filter(__cellMatches,cells)))
    print 'Houses created'
    print 'Starting Grid creation'
    grid = structures.Grid.Grid(cells,houses)
    print 'Grid created'
    print 'Trying to solve'
    solver.Solver.HiddenSingleSolver.solve(grid)
    print 'Solving finished'
    print 'Done!'

if __name__ == "__main__":
    tryConstruct()