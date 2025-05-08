import pygame
pygame.init()
black = (0,0,0)

screen = pygame.display.set_mode((1200,800))
image = pygame.image.load('Angry_Bird.png').convert()
clock= pygame.time.Clock()

x= 100
y = 200
done = False

while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done= True
    x += 4

    screen.fill(black)
    screen.blit(image, (x,y))
    pygame.display.update()
    clock.tick(60)
pygame.quit()