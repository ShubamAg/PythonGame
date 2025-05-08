'''import pygame
pygame.init()

size = (400,400)

display = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False
press = False

while not done:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done= True
             px,py = pygame.mouse.get_pos()
        if event.type ==pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(surface=display, color=(255,255,255), center=(px,py), radius=30)

        if event.type == pygame.MOUSEBUTTONUP:
            press = False
        pygame.display.update()
        clock.tick(30)
    except Exception as e:
    print(Exception)
    pygame.quit()
quit()'''
#we need to have if then elif you retard. Also JUST DIE ALREADY!!
'''import pygame
pygame.init()

size = (400, 400)
display = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False
press = False

while not done:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                px, py = pygame.mouse.get_pos()
                pygame.draw.circle(surface=display, color=(255, 255, 255), center=(px, py), radius=30)

            elif event.type == pygame.MOUSEBUTTONUP:
                press = False

        pygame.display.update()
        clock.tick(30)

    except Exception as e:
        print("Error:", e)

pygame.quit()
quit()'''

#Drawing custom Triangles
'''import pygame
pygame.init()

size = (400, 400)
display = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False

while not done:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                px, py = pygame.mouse.get_pos()

                # Triangle points relative to click
                points = [(px, py), (px + 100, py + 100), (px - 20, py + 20)] 
                pygame.draw.polygon(surface=display, color=(0, 255, 0), points=points)

            elif event.type == pygame.MOUSEBUTTONUP:
                pass  # No action needed

        pygame.display.update()
        clock.tick(30)

    except Exception as e:
        print("Error:", e)

pygame.quit()
quit()
'''

import pygame
pygame.init()

size = (900, 900)
display = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

done = False
selected_shape = "Circle"

# Simple buttons
def draw_menu():
    pygame.draw.rect(display, (200, 200, 200), (10, 10, 100, 30))
    pygame.draw.rect(display, (200, 200, 200), (120, 10, 100, 30))
    pygame.draw.rect(display, (200, 200, 200), (230, 10, 100, 30))

    display.blit(font.render("Circle", True, (0, 0, 0)), (25, 15))
    display.blit(font.render("Square", True, (0, 0, 0)), (135, 15))
    display.blit(font.render("Triangle", True, (0, 0, 0)), (245, 15))

def draw_shape(shape, pos):
    x, y = pos
    if shape == "Circle":
        pygame.draw.circle(display, (255, 0, 0), (x, y), 30)
    elif shape == "Square":
        pygame.draw.rect(display, (0, 255, 0), (x - 30, y - 30, 60, 60))
    elif shape == "Triangle":
        points = [(x, y - 30), (x - 30, y + 30), (x + 30, y + 30)]
        pygame.draw.polygon(display, (0, 0, 255), points)

while not done:
    display.fill((0, 0, 0))
    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            # Shape selection buttons
            if 10 <= mx <= 110 and 10 <= my <= 40:
                selected_shape = "Circle"
            elif 120 <= mx <= 220 and 10 <= my <= 40:
                selected_shape = "Square"
            elif 230 <= mx <= 330 and 10 <= my <= 40:
                selected_shape = "Triangle"
            elif my > 50:  # Don't draw if clicking on menu
                draw_shape(selected_shape, event.pos)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
