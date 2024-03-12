import random

class Cell:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.isStart = False
        self.isFinal = False
        self.isVisited = False
        self.neighbors = set()
        self.walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }
    
    def addNeighbor(self, neighbor):
        self.neighbors.add(neighbor)
        neighbor.neighbors.add(self)
    
    def addPathToNeighbor(self, neighbor):
        # the logic is reversed because of how 2d array works
        if(neighbor.col > self.col):
            self.walls["right"] = False
            neighbor.walls["left"] = False
        elif(neighbor.col < self.col):
            self.walls["left"] = False
            neighbor.walls["right"] = False
        elif(neighbor.row > self.row):
            self.walls["bottom"] = False
            neighbor.walls["top"] = False
        elif(neighbor.row < self.row):
            self.walls["top"] = False
            neighbor.walls["bottom"] = False
    
    def __eq__(self, compCell):
        return self.col == compCell.col and self.row == compCell.row
    
    def __hash__(self):
        return hash((self.col, self.row))

    def toString(self):
        output = ""
        if self.walls["left"]: 
            output += "|"
        if self.walls["top"]:
            output += "^"

        if self.isStart: 
            output += "1"
        elif self.isFinal:
            output += "2"
        else:
            output += "0"

        if self.walls["bottom"]:
            output += "v"
        if self.walls["right"]:
            output += "|"

        return output


def createStartingPoint(mazeSize):
    output = {"col": -1, "row": -1}

    #randing is inclusive of right
    startingWall = random.randint(0, mazeSize-1)
    startingPosition = random.randint(0, mazeSize-1)

    # top right bottom left
    if(startingWall == 0):
        output["col"] = startingPosition
        output["row"] = 0
    elif(startingWall == 1):
        output["col"] = mazeSize-1
        output["row"] = startingPosition
    elif(startingWall == 2):
        output["col"] = startingPosition
        output["row"] = mazeSize-1
    elif(startingWall == 3):
        output["col"] = 0
        output["row"] = startingPosition
    
    return output

def getViableNeighbor(cell):
    validNeighbors = []
    for neighbor in cell.neighbors:
        if not neighbor.isVisited:
            validNeighbors.append(neighbor)
    
    if len(validNeighbors) == 0:
        return None
    return validNeighbors[random.randint(0, len(validNeighbors)-1)]
