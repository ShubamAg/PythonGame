import pygame
pygame.init()

size = [500,400]
display = pygame.display.set_mode(size)
pygame.display.set_caption("Drawing pr")

finish = False
clock = pygame.time.Clock()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    clock.tick(20)

#set screen background
#while setting the display color we have to use two (())
#We can also define the colors in the code above and then use the string for them. i.e To use Black color we need to define it first by
#Black= (0,0,0)
    display.fill((255,255,255))

    #creating rectangle with outline
    pygame.draw.rect(surface=display, color= (0,0,255), rect= [85,10,20,40], width=2)
    #creating solid rect
    pygame.draw.rect(surface=display, color= (255,30,10), rect= [120,60,30,70])

    pygame.display.update()
pygame.quit()
