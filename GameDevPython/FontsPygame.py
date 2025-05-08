import pygame
pygame.init()
Black = (0,0,0)

disp = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
finished = False
#Font family adn the size of it
#If you want to know what font you can use, we can run the code>>
#font= pygame.font.get_font() print(font)// This will print the list of all the system fonts we can use in the code.
'''f= pygame.font.get_fonts()
print(f)'''
font = pygame.font.SysFont("comicsansms", 72) 
text= font.render("Game", True, (0,255,0))

font = pygame.font.SysFont("chiller", 40)
text1 = font.render('You Died', True,  (255,255,255))

while not finished:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            finished = True
        
    disp.fill(Black)
    disp.blit(text, (100,200))
    disp.blit(text1, (200,380))

    pygame.display.flip()
    clock.tick(60)
pygame.display.quit()