import pygame
pygame.init()
screen=pygame.display.set_mode((500,600))
done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    pygame.draw.rect(screen, (153,51,102), pygame.Rect(0,0,60,60))

    pygame.display.flip()
