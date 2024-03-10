import maze
import pygame

square_size = 50

pygame.init()
screen = pygame.display.set_mode((square_size * maze.size + square_size, 
    square_size * maze.size + square_size))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #render
    for row in range(len(maze.maze_array)):
        for col in range(len(maze.maze_array[0])):
            pygame.draw.line(screen, "white", (col * square_size, row * square_size), 
                (col * square_size + square_size, row * square_size))
            pygame.draw.line(screen, "white", (col * square_size, row * square_size), 
                (col * square_size, row * square_size  + square_size))
            pygame.draw.line(screen, "white", (col * square_size + square_size, row * square_size), 
                (col * square_size + square_size, row * square_size  + square_size))
            pygame.draw.line(screen, "white", (col * square_size, row * square_size + square_size), 
                (col * square_size + square_size, row * square_size + square_size))

    pygame.display.flip()

pygame.quit()




