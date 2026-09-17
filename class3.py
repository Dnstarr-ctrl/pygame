import pygame
import random
pygame.init()
#creating custom ids
event1=pygame.USEREVENT + 1
event2=pygame.USEREVENT + 2
BlueColor=pygame.Color("blue")
RedColor=pygame.Color("red")
YellowColor=pygame.Color("yellow")



#sprite colours ---
BrownColor=pygame.Color("brown")
Grey=pygame.Color("grey")
Green=pygame.Color("green")

class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface(width,height)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]


Screen= pygame.display.set_mode((500,500))
done= False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

