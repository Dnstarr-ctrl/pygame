import pygame
pygame.init()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
display_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tiger Elegancy")
background = pygame.transform.scale(pygame.image.load("ooh.jpeg").convert(),(500, 500))
pic = pygame.transform.scale(pygame.image.load("new.jpeg").convert_alpha(),(220, 220))

rect1 = pic.get_rect(center=(250, 220))
headfont = pygame.font.Font(None, 42)
factfont = pygame.font.Font(None, 28)
headtext = headfont.render("Wildlife Elegancy: Tiger!",True,pygame.Color("black"))
heading_rect = headtext.get_rect(center=(250, 45))
facttext = factfont.render("Tigers are very powerful wild cats which live in jungle they are carnivorous.",True,pygame.Color("black"))
 

factrect = facttext.get_rect(center=(250, 420))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background,(0, 0))
        display_surface.blit(pic,rect1)
        display_surface.blit(headtext,heading_rect)
        display_surface.blit(facttext,factrect)

        pygame.display.flip()
        clock.tick(30)
        pygame.quit()
        
 
if __name__ == "__main__":
    game_loop()
