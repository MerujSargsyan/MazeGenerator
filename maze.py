import sys
import util

if len(sys.argv) != 2:
    print("Please enter the size of the maze")
    sys.exit()

mazeSize = int(sys.argv[1])

mazeArray = [[None] * mazeSize for _ in range(mazeSize)]

startingPoint = util.createStartingPoint(mazeSize)

def generateMaze():
    for row in range(mazeSize):
        for col in range(mazeSize):
            current = util.Cell(row, col)
            if col - 1 >= 0:
                current.addNeighbor(mazeArray[row][col-1])
            if startingPoint["col"] == col and startingPoint["row"] == row:
                current.isStarting = True
            mazeArray[row][col] = current
    
    current = mazeArray[startingPoint["row"]][startingPoint["col"]]
    # implemented array as stack
    stack = []
    visitedCount = 0

    stack.append(current)
    while len(stack) > 0:
        current.isVisited = True
        visitedCount += 1
        neighbor = util.getViableNeighbor(current)
        if neighbor is None:
            # checks if every cell is visited
            if visitedCount == mazeSize * mazeSize:
                current.isFinal = True
            current = stack.pop()
        else:
            current.addPathToNeighbor(neighbor)
            stack.append(current)
            current = neighbor

    
def connectBottomNeighbors():
    for row in range(mazeSize):
        for col in range(mazeSize):
            current = mazeArray[row][col]
            
            if row + 1 < mazeSize:
                current.addNeighbor(mazeArray[row+1][col])

def printMaze():
    output = "\n"
    for i in range(mazeSize):
        output += "["

        for j in range(mazeSize):
            cell = mazeArray[i][j]
            output += cell.toString() + ", "
        output += "]\n"
        print(output)

generateMaze()
printMaze()