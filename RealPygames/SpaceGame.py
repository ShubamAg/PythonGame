#Importing All the libraries we will need and initializing them
import pygame
import time
import random
pygame.font.init()
pygame.init()

#Setting the screen or window of the game and setting the caption of the window
Width, Hight = 1200, 800

disp = pygame.display.set_mode((Width, Hight))
'''in the pygame the top left of the screen is (0,0) and top right right is width. Same is vice versa
The coordinate of Y start from top and goes up while going down the screen'''

pygame.display.set_caption("Space Game")

#Initializing the width and height of the player with velocity and fonts for the game
Player_width = 70
Player_hight = 70
Player_Vel= 5
Star_width = 25
Star_height = 25
Star_vel = 3
Font = pygame.font.SysFont("comicsans", 25)


#Setting the background of our game
BG = pygame.transform.scale(pygame.image.load("BackGround.jpg"),(1200,800) )
Player_img= pygame.image.load("Plane2D.png").convert_alpha()
Meteor_img= pygame.image.load("Meteor2D.png").convert_alpha()

Player_img = pygame.transform.scale(Player_img, (Player_hight, Player_width))
Meteor_img = pygame.transform.scale(Meteor_img, (Star_height, Star_width))


#creating a simple function to have all the basic things like player and timer
def draw(player, elapsed_time, stars):
    disp.blit(BG, (0,0))
    
    time_text = Font.render( f"time : {round (elapsed_time)}s", 1, "white" )
    disp.blit(time_text, (10,10))
    
    #player
    #pygame.draw.rect(disp, "red", player)
    disp.blit(Player_img, (player.x, player.y))

    for star in stars:
        #pygame.draw.rect(disp, "white", star)
        disp.blit(Meteor_img, (star.x, star.y))

    pygame.display.update()


#creating a main() function to have essintial things of the game
def main():
    running = True
    player = pygame.Rect(200, Hight - Player_hight, Player_width, Player_hight)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment= 2000
    star_count = 0

    stars= []
    hit = False


#starting the main loop for the game which will keep the game running and take the user's input
    while running:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(4):
                star_x = random.randint(0, Width - Star_width)
                star = pygame.Rect(star_x, -Star_height, Star_height, Star_width)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count=0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - Player_Vel >= 0:
            player.x -= Player_Vel

        if keys[pygame.K_RIGHT] and player.x + Player_Vel+Player_width<= Width:
            player.x += Player_Vel

        for star in stars [:]:
            star.y += Star_vel
            if star.y > Hight:
                stars.remove(star)
            elif star.y * Star_height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

            if hit:
                lost_text = Font.render("You Lost!", 1, "white")
                score_text = Font.render(f"You lasted: {round(elapsed_time)} seconds", 1, "white")
                
                disp.blit(lost_text, (Width/2 - lost_text.get_width()/2, Hight/2 - lost_text.get_height()/2 - 30))
                disp.blit(score_text, (Width/2 - score_text.get_width()/2, Hight/2 - score_text.get_height()/2 + 30))
                
                pygame.display.update()
                pygame.time.delay(7000)
                main()
                return

        


        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()