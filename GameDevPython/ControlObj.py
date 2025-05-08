#First try with moving object

'''import pygame
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,800))

x= 10
y= 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.K_w:
            y+= 5
    elif event.type == pygame.K_a:
            x -= 5
    elif event.type == pygame.K_s:
            y -= 5
    elif event.type == pygame.K_d:
            x += 5
    screen.fill((0,0,0))
    clock.tick(40)
    pygame.draw.circle(surface=screen, color=(255,255,255), center=(x,y), radius=40)
    pygame.display.update()
pygame.quit()
'''

#=======================================================
#=======================================================
# Moving the object 

'''import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))

x=20
y=20
running= True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hit = pygame.key.get_pressed()
    if hit[pygame.K_w]:
        y -=5
    if hit[pygame.K_a]:
        x -=5
    if hit[pygame.K_s]:
        y +=5
    if hit[pygame.K_d]:
        x +=5
    screen.fill((0,0,0))
    clock.tick(40)
    pygame.draw.circle(surface=screen, color=(255,255,255), center=(x,y), radius=40)
    pygame.display.update()
pygame.quit()'''

#=======================================================
#=======================================================
#A simple maze game

import pygame
pygame.init()
clock = pygame.time.Clock()

#Setting up the maze (0 = path, 1 = wall)
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1],
    [1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1],
    [1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 60
screen = pygame.display.set_mode((16*TILE_SIZE, 13*TILE_SIZE)) #here the first TILE_SIZE is rows, and second TILE_SIZE is cols
player_x = 1
player_y = 1

finish_x = 14
finish_y = 1

game_won = False

#Starting loop for user input
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    new_x = player_x
    new_y = player_y

    if keys[pygame.K_w]:
        new_y -= 1
    elif keys[pygame.K_s]:
        new_y += 1
    elif keys[pygame.K_a]:
        new_x -= 1
    elif keys[pygame.K_d]:
        new_x += 1

    # Check if the object is hitting the wall
    if maze[new_y][new_x] == 0:
        player_x = new_x
        player_y = new_y

    screen.fill((0, 0, 0))

    # Drawing maze
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            color = (200, 200, 200) if maze[y][x] == 1 else (50, 50, 50)
            pygame.draw.rect(screen, color, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    #Drwaing finishing tile        
    pygame.draw.rect(screen, (0, 255, 0), (finish_x*TILE_SIZE, finish_y*TILE_SIZE, TILE_SIZE, TILE_SIZE))


    # Drawing player
    pygame.draw.circle(screen, (255, 255, 0), (player_x*TILE_SIZE + TILE_SIZE//2, player_y*TILE_SIZE + TILE_SIZE//2), 20)

    if game_won:
        text = pygame.font.render("You completed the game!", True, (255,0,0))
        screen.blit(text, (50, 250))

    pygame.display.update()
    clock.tick(10)

pygame.quit()

#=======================================================
#=======================================================
#A simple maze game with finish line

'''import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))

# Maze setup (0 = path, 1 = wall)
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,1],
    [1,1,0,1,0,1,1,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 60
player_x = 1
player_y = 1

# Set finish line (x, y)
finish_x = 8
finish_y = 8

font = pygame.font.SysFont(None, 48)
game_won = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_won:
        keys = pygame.key.get_pressed()
        new_x = player_x
        new_y = player_y

        if keys[pygame.K_w]:
            new_y -= 1
        elif keys[pygame.K_s]:
            new_y += 1
        elif keys[pygame.K_a]:
            new_x -= 1
        elif keys[pygame.K_d]:
            new_x += 1

        # Check wall collision
        if maze[new_y][new_x] == 0:
            player_x = new_x
            player_y = new_y

        # Check if player reached finish
        if player_x == finish_x and player_y == finish_y:
            game_won = True

    screen.fill((0, 0, 0))

    # Draw maze
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            color = (200, 200, 200) if maze[y][x] == 1 else (50, 50, 50)
            pygame.draw.rect(screen, color, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw finish tile
    pygame.draw.rect(screen, (0, 255, 0), (finish_x*TILE_SIZE, finish_y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw player
    pygame.draw.circle(screen, (255, 255, 0), (player_x*TILE_SIZE + TILE_SIZE//2, player_y*TILE_SIZE + TILE_SIZE//2), 20)

    # If won, show message
    if game_won:
        text = font.render("You completed the game!", True, (255,0,0))
        screen.blit(text, (50, 250))

    pygame.display.update()
    clock.tick(10)

pygame.quit()'''

#=======================================================
#=======================================================
