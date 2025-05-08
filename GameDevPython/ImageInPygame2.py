#The code is not working properly as well. The events such as 1,0,l and s are not happening. Just like the above code.
#<<--ChatGPT Code-->>

'''import pygame
import os
import cv2
from pygame.locals import *

Pink = (255, 123, 255)
Black = (0, 0, 0)

pygame.init()

disp = (600, 600)
display = pygame.display.set_mode(disp)

# Load and convert image correctly
picture_original = pygame.image.load('Darthvader.jpg').convert()
rect = picture_original.get_rect()
pygame.draw.rect(picture_original, Pink, rect, 10)

# Set base variables
angle = 0
scale = 0.5
img = pygame.transform.rotozoom(picture_original, angle, scale)
rect = img.get_rect()
center = (disp[0] // 2, disp[1] // 2)
rect.center = center

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        elif event.type == pygame.KEYDOWN:
            # Rotate
            if event.key == pygame.K_q:
                if event.mod & pygame.KMOD_SHIFT:
                    angle -= 20
                else:
                    angle += 20

            # Zoom
            elif event.key == pygame.K_t:
                if event.mod & pygame.KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1

            # Reset
            elif event.key == pygame.K_o:
                angle = 0
                scale = 0.5
                img = pygame.transform.rotozoom(picture_original, angle, scale)

            # Flip horizontal
            elif event.key == pygame.K_0:
                img = pygame.transform.flip(img, True, False)

            # Flip vertical
            elif event.key == pygame.K_1:
                img = pygame.transform.flip(img, False, True)

            elif event.key == pygame.K_l:
                img = cv2.imread('Darthvader.jpg')
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                edges = cv2.Laplacian(gray, cv2.CV_64F)
            # Scale2x
            elif event.key == pygame.K_s:
                img = pygame.transform.scale2x(img)

            # Rotate fixed 90°
            elif event.key == pygame.K_r:
                img = pygame.transform.rotate(img, 90)

            # Apply base rotation + scale from original image (if angle/scale changed)
            else:
                img = pygame.transform.rotozoom(picture_original, angle, scale)

            # Update image center
            rect = picture_original.get_rect()
            rect.center = center

    display.fill(Black)
    display.blit(picture_original, rect)
    pygame.display.update()

pygame.quit()'''

#=======================================================
#=======================================================
'''import pygame
import cv2
import numpy as np
from pygame.locals import *

Pink = (255, 123, 255)
Black = (0, 0, 0)

pygame.init()
disp = (600, 600)
display = pygame.display.set_mode(disp)

# Load image with pygame and keep original
picture = pygame.image.load('Darthvader.jpg').convert()
original_picture = picture.copy()

# Draw pink border (optional)
rect = picture.get_rect()
pygame.draw.rect(picture, Pink, rect, 10)

# Init state
img = picture.copy()
angle = 0
scale = 1 / 2
center = (disp[0] // 2, disp[1] // 2)
use_opencv_image = False

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        elif event.type == pygame.KEYDOWN:
            # Rotation (Q)
            if event.key == pygame.K_q:
                if event.mod & pygame.KMOD_SHIFT:
                    angle -= 20
                else:
                    angle += 20

            # Zoom (T)
            elif event.key == pygame.K_t:
                if event.mod & pygame.KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1

            # Reset (O)
            elif event.key == pygame.K_o:
                img = original_picture.copy()
                angle = 0
                scale = 1 / 2
                use_opencv_image = False

            # Flip horizontally (0)
            elif event.key == pygame.K_0:
                img = pygame.transform.flip(img, True, False)

            # Flip vertically (1)
            elif event.key == pygame.K_1:
                img = pygame.transform.flip(img, False, True)

            # Apply Laplacian edge detection using OpenCV (L)
            elif event.key == pygame.K_l:
                cv_img = cv2.imread('Darthvader.jpg')
                gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
                edges = cv2.Laplacian(gray, cv2.CV_8U)
                # Convert OpenCV image to Pygame surface
                edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
                edges_rgb = cv2.resize(edges_rgb, disp)
                img_surface = pygame.image.frombuffer(edges_rgb.tobytes(), disp, 'RGB')
                img = img_surface
                use_opencv_image = True

            # Scale2x (S)
            elif event.key == pygame.K_s:
                img = pygame.transform.scale2x(img)

            # Rotate by 90° (R)
            elif event.key == pygame.K_r:
                img = pygame.transform.rotate(img, 90)

    # Only apply rotozoom if we're not using OpenCV-processed image
    if not use_opencv_image:
        img = pygame.transform.rotozoom(picture, angle, scale)

    # Update position
    rect = img.get_rect()
    rect.center = center

    # Redraw
    display.fill(Black)
    display.blit(img, rect)
    pygame.display.update()

pygame.quit()'''

#=======================================================
#=======================================================
'''import pygame
import cv2
import numpy as np
from pygame.locals import *

Pink = (255, 123, 255)
Black = (0, 0, 0)

pygame.init()
disp = (600, 600)
display = pygame.display.set_mode(disp)

# Load image
picture = pygame.image.load('Darthvader.jpg').convert()
original_picture = picture.copy()

# Draw pink border (optional)
rect = picture.get_rect()
pygame.draw.rect(picture, Pink, rect, 10)

img = picture.copy()
angle = 0
scale = 0.5
center = (disp[0] // 2, disp[1] // 2)
use_opencv_image = False

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                angle += 20 if not (event.mod & pygame.KMOD_SHIFT) else -20

            elif event.key == pygame.K_t:
                scale *= 1.1 if not (event.mod & pygame.KMOD_SHIFT) else 1 / 1.1

            elif event.key == pygame.K_o:
                img = original_picture.copy()
                picture = original_picture.copy()
                angle = 0
                scale = 0.5
                use_opencv_image = False

            elif event.key == pygame.K_0:
                img = pygame.transform.flip(img, True, False)

            elif event.key == pygame.K_1:
                img = pygame.transform.flip(img, False, True)
        
        #Laplacian
            elif event.key == pygame.K_l:
                cv_img = cv2.imread('Darthvader.jpg')
                gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
                edges = cv2.Laplacian(gray, cv2.CV_8U)
                edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
                edges_rgb = cv2.resize(edges_rgb, disp)
                img = pygame.image.frombuffer(edges_rgb.tobytes(), disp, 'RGB')
                use_opencv_image = True

            elif event.key == pygame.K_s:
                img = pygame.transform.scale2x(img)

            elif event.key == pygame.K_r:
                img = pygame.transform.rotate(img, 90)

    # Apply rotation and scale only if not using OpenCV output
    if not use_opencv_image:
        img = pygame.transform.rotozoom(picture, angle, scale)

    # Center and draw
    rect = img.get_rect()
    rect.center = center

    display.fill(Black)
    display.blit(img, rect)
    pygame.display.update()

pygame.quit()'''