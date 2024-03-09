import sys
import random 

if len(sys.argv) != 2:
    print("Please enter the size of the maze")
    sys.exit()

size = int(sys.argv[1])

maze_array = [[1]*size for _ in range(size)]

def generate_maze():
    start_idx = random.randint(0, size-1)
    end_idx = random.randint(start_idx, size-1)

    maze_array[0][start_idx] = 0
    maze_array[end_idx][0] = 0

    starting_point = maze_array[0][start_idx]
    