#imorting libraries
import pygame
#initialize pygame
pygame.init()
#creating window
gamed= pygame.display.set_mode((400,200))
#set display
pygame.display.set_caption("My first pygame")
#set time
clock= pygame.time.Clock()
stop= False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    pygame.display.update()
   #if we want to speed up the game, we use clock.click()
   # clock.click(40)
#to quit the application
pygame.quit()