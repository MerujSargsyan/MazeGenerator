import maze
import pygame

square_size = 50

pygame.init()
screen = pygame.display.set_mode((square_size * maze.mazeSize, square_size * maze.mazeSize))
running = True

maze.generateMaze()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #render
    screen.fill("black")
    for row in range(maze.mazeSize):
        for col in range(maze.mazeSize):
            cell = maze.mazeArray[row][col]
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




