import maze
import pygame

square_size = 50

pygame.init()
screen = pygame.display.set_mode((square_size * maze.size + square_size, 
    square_size * maze.size + square_size))
running = True

maze.start_maze_generation()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #render
    for row in range(len(maze.maze_array)):
        for col in range(len(maze.maze_array[0])):
            cell = maze.maze_array[row][col]
            walls = cell.walls
            color = "white"
            if cell.isStart:
                color = "green"

            if walls["top"]:
                pygame.draw.line(screen, color, (col * square_size, row * square_size), 
                    (col * square_size + square_size, row * square_size))
            if walls["left"]:
                pygame.draw.line(screen, color, (col * square_size, row * square_size), 
                    (col * square_size, row * square_size  + square_size))
            if walls["right"]:
                pygame.draw.line(screen, color, (col * square_size + square_size, row * square_size), 
                    (col * square_size + square_size, row * square_size  + square_size))
            if walls["left"]:
                pygame.draw.line(screen, color, (col * square_size, row * square_size + square_size), 
                    (col * square_size + square_size, row * square_size + square_size))

    pygame.display.flip()

pygame.quit()




