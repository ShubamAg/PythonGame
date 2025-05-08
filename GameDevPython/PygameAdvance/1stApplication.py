import pygame
pygame.init()

screen =  pygame.display.set_mode((600,600))

clock = pygame.time.Clock()

right_run = [pygame.image.load('run1'), pygame.image.load('run2'),pygame.image.load('run3'),pygame.image.load('run4'),pygame.image.load('run5'),pygame.image.load('run6'),pygame.image.load('run7'),pygame.image.load('run8'),pygame.image.load('run9')]
bg = pygame.image.load('BG2.jpg')
standing =  pygame.image.load('run1')

running = True
x=100
y=250
w=40
inc= 10
count_run = 10
count_jump = 10
jump= False
right = False
left = False

def fun_draw():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        hit = pygame.key.get_pressed()
        if hit[pygame.K_d] and x> inc:
            x -= inc
            left = False
            right = True
            