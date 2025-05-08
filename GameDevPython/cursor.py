import pygame
import sys
from pygame.locals import *
pygame.init()

srn = pygame.display.set_mode((1200,800))

img= 'star.png'
cursor= pygame.image.load(img)

while not False:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
        srn.fill ((255,255,255))
        x , y = pygame.mouse.get_pos()
        x-= cursor.get_width()/2
        y-= cursor.get_height()/2

    srn.blit(cursor, (x,y))
    pygame.display.update()
