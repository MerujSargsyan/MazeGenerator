import maze
import pygame

square_size = 50

pygame.init()
screen = pygame.display.set_mode((square_size * maze.size, square_size * maze.size))
running = True

maze.start_maze_generation()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #render
    for row in range(len(maze.maze_array)):
        for col in range(len(maze.maze_array[row])):
            cell = maze.maze_array[row][col]
            walls = cell.walls

            if walls["right"]:
                pygame.draw.line(screen, "white", 
                    (cell.x * square_size + square_size, cell.y * square_size), 
                    (cell.x * square_size + square_size, cell.y * square_size + square_size))
            if walls["left"]:
                pygame.draw.line(screen, "white",
                    (cell.x * square_size, cell.y * square_size), 
                    (cell.x * square_size, cell.y * square_size + square_size))
            if walls["top"]:
                pygame.draw.line(screen, "white",
                    (cell.x * square_size, cell.y * square_size),
                    (cell.x * square_size + square_size, cell.y * square_size))
            if walls["bottom"]:
                pygame.draw.line(screen, "white",
                    (cell.x * square_size, cell.y * square_size + 25),
                    (cell.x * square_size + square_size, cell.y * square_size + square_size))
    pygame.display.flip()

pygame.quit()




