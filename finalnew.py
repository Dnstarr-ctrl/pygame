import pygame
import random
 
Width,Height = 500, 400
Speed = 5
FontSize = 60
 
pygame.init()
 
background_image = pygame.transform.scale(pygame.image.load("pet_bg.jpg"),(Width, Height))
 
font = pygame.font.SysFont("Arial",FontSize)
class Sprite(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change,Width - self.rect.width),0)
 
        self.rect.y = max(
            min(self.rect.y + y_change,Height - self.rect.height),0)
 
screen = pygame.display.set_mode((Width, Height))
 
pygame.display.set_caption("Pet Food Collection Game")
sprites = pygame.sprite.Group()
 

pet = Sprite(pygame.Color("brown"),40,40)
 
pet.rect.x = 30
pet.rect.y = 180
sprites.add(pet)
pet_food = Sprite(pygame.Color("orange"),30,30)
pet_food.rect.x = random.randint(100,Width - pet_food.rect.width)
 
pet_food.rect.y = random.randint(0,Height - pet_food.rect.height)
sprites.add(pet_food)

running = True
food_collected = False

clock = pygame.time.Clock()
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if not food_collected:
                keys = pygame.key.get_pressed()
                xchange = (keys[pygame.K_RIGHT] -keys[pygame.K_LEFT]) * Speed
 
        ychange = (keys[pygame.K_DOWN] -keys[pygame.K_UP]) * Speed
        pet.move(xchange,ychange)

        if pet.rect.colliderect(pet_food.rect):
            sprites.remove(pet_food)
            foodcollected = True
 
    screen.blit(background_image,(0, 0))
 
    sprites.draw(screen)
 
    if foodcollected:
        win_text = font.render("Food Collected!",True,pygame.Color("black"))
        text_x = (Width -win_text.get_width()) // 2
        text_y = (Height -win_text.get_height()) // 2
        screen.blit(win_text,(text_x, text_y))
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
