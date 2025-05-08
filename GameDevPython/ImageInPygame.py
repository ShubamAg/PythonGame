#Basics-->
'''Loading the image>>
    pygame.image.load(path)
    image.convert()
    pygame.image.save()

Flipping the image>>
    flip(surface, xbool, ybool)
    image, tru false: Horizental
    image, false, true: Verticle

Rotate>>
    rotate()

Rotozoom>>
    rotozoom()

Scale>>
    pygame.transform.scale2x()
    scale2x(surface, Destsurfae = none)

Laplacian>>To found out the edges of the images or surface.
    laplacian(surface, destsurface = none)'''


#==========================================================
#Having an image in the display and performing task on that image based on users input.

'''import pygame
import os
from pygame.locals import *

Pink = (255,123,255)
Black = (0,0,0)

pygame.init()

disp = (600,600)

display = pygame.display.set_mode(disp)
picture = pygame.image.load('Darthvader.jpg')
picture.convert()

rect = picture.get_rect()
pygame.draw.rect(picture, Pink, rect, 10)

img= picture
rect = img.get_rect()
center = (disp[0]//2 , disp[1]//2)
rect.center = center 

done = True
angle = 0
scale = 1/2

while done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done= False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if event.mod & pygame.KMOD_SHIFT:
                    angle -= 20
                else:
                    angle += 20

            elif event.key == pygame.K_t:
                    if event.mod & pygame.KMOD_SHIFT:
                        scale /= 1.1
                    else:
                        scale *= 1.1
                
            elif event.key == pygame.K_o:
                    img = picture
                    angle = 0
                    scale = 1/2

            elif event.key == pygame.K_0:
                img = pygame.transform.flip(img, True, False)

            elif event.key == pygame.K_1:
                img = pygame.transform.flip(img, False, True)

            elif event.key == pygame.K_l:
                img = pygame.transform.laplacian(img)

            elif event.key == pygame.K_s:
                img = pygame.transform.scale2x(img)

            elif event.key == pygame.K_r:
                img = pygame.transform.rotate(img, 90)
        
        img = pygame.transform.rotozoom(picture, angle, scale)
        rect = img.get_rect()
        rect.center = (disp[0]//2, disp[1]//2)

    display.fill(Black)
    display.blit(img, rect)
    pygame.display.update()
pygame.quit()'''

#==========================================================
#==========================================================
