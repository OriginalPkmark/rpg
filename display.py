import pygame

pygame.init()

# Default display size
width = 800
height = 600

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.display.set_caption("My RPG Game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            pygame.display.set_caption("My RPG Game")

    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()
