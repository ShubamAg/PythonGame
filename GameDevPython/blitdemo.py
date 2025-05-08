import pygame
pygame.init()

#creating the canvas
display = [400,400]
scr = pygame.display.set_mode(display)

surf = pygame.Surface((200,200)) #here we have to give another value for the Surface instead of just giving src or something else.

#creating objects
pygame.draw.rect(surface= surf, color=(0,0,255), rect=(100,30,60,90,))
pygame.draw.circle(surface=surf, color=(255,255,255), center=(40,100), radius=40)

scr.blit(surf,(10,30))

pygame.display.update()

#create a while loop for iteration
finish= 0
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish=True
pygame.quit()
