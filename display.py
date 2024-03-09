import maze
import pygame

square_size = 50

pygame.init()
screen = pygame.display.set_mode((square_size * maze.size, square_size * maze.size))
running = True

maze.generate_maze()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #render
    for row in range(len(maze.maze_array)):
        for col in range(len(maze.maze_array[row])):
            #black for 0 and white for 1
            color = 255 * maze.maze_array[row][col]
            rectColor = (color, color, color)
            recPos = (row * square_size, col * square_size, square_size, square_size)
            pygame.draw.rect(screen, rectColor, recPos)

    pygame.display.flip()

pygame.quit()




