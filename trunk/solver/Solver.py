import structures.Grid
import AbstractSolver

class HiddenSingleSolver(AbstractSolver.AbstractSolver):
    @staticmethod
    def solve(grid):
        #TODO: make it possible to order differently
        for i in grid.houses:
            counter = 0
            maxValue = i.cells[0].maxValue
            available = range(maxValue)[1:]
            candidateCells = []
            for j in i.cells:
                if(len(j.value)>1):
                    counter = counter+1
                    candidateCells.append(j)
                elif(len(j.value)==1):
                    try:
                        available.remove(j.value[0:0])
                    except ValueError:
                        'blah'
            if(counter == 1 and len(available)==1):
                j.value = []
                j.value.append(available[0:0])