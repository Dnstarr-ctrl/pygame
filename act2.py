import pygame
pygame.init()
screen=pygame.display.set_mode((400,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.circle(screen, (0,255,0), (300,300), 50)
    pygame.draw.circle(screen, (255,0,0), (300,300), 50, 5)
    pygame.display.flip()