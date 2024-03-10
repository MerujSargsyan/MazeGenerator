import sys
import random

if len(sys.argv) != 2:
    print("Please enter the size of the maze")
    sys.exit()

size = int(sys.argv[1])

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.walls = {'top': True, 'right': True, 'bottom': True,
            'left': True}
        self.visited = False
        self.isStart = False
    
    def get_neighbor(self):
        valid_neighbors = []
        if(self.x+1 < size):
            valid_neighbors.append(maze_array[self.y][self.x+1])
        if(self.x-1 >= 0):
            valid_neighbors.append(maze_array[self.y][self.x-1])
        if(self.y-1 >= 0):
            valid_neighbors.append(maze_array[self.y-1][self.x])
        if(self.y+1 < size):
            valid_neighbors.append(maze_array[self.y+1][self.x])
        
        for neighbor in valid_neighbors:
            if neighbor.visited == False:
                return neighbor
        
        return None


maze_array = [[None] * size for _ in range(size)]

for row in range(len(maze_array)):
    for col in range(len(maze_array[0])):
        maze_array[row][col] = Cell(col, row)

print(len(maze_array))
print(len(maze_array[0]))



def start_maze_generation():
    start_idx = random.randint(0, size-1)

    start_cell = maze_array[0][start_idx]
    start_cell.isStart = True
    generate_maze((start_cell.x, start_cell.y))

visited = []
def generate_maze(starting_pos):
    x,y = starting_pos

    while len(visited) < size*size:
        cell = maze_array[x][y]
        neighbor = cell.get_neighbor()
        neighbor.visitied = True
        if neighbor is not None:
            visited.append(neighbor)
            connect(cell, neighbor)
        else:
            x,y = (visited.pop().x, visited.pop().y)
    


def connect(cell1, cell2):
    if cell1.x < cell2.x:
        cell1.walls['right'] = False
        cell2.walls['left'] = False
    elif cell1.x > cell2.x:
        cell1.walls['left'] = False
        cell2.walls['right'] = False
    elif cell1.y > cell2.y:
        cell1.walls['bottom'] = False
        cell2.walls['top'] = False
    elif cell1.y < cell2.y:
        cell1.walls['top'] = False
        cell2.walls['bottom'] = False



    



    