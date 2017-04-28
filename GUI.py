import pygame                                                                       #Henry Chen
import sys
import random                                                                   # Q: Why can't you take an atom seriously?
from PlayerClass import PlayerClass                                             # A: Because they make up everything!
import view_Background
from view_Player import view_Player
from Zombie import Zombie
from Bullet import Bullet

pygame.init()
BLACK = (0, 0, 0)

clock = pygame.time.Clock()                                                         #Used to manage how fast the screen updates

screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('Zombie Apocalypse')

background_position = [0,0]
background_image = pygame.image.load("background.png").convert()

# --- Sprite Lists ---
all_sprites_list = pygame.sprite.Group()
zombie_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

# --- Create Player Sprite ---
player_sprite = view_Player(800, 600)
player = PlayerClass()
all_sprites_list.add(player_sprite)


# --- Variables ---
score = 0
bullet_count = 10
zombie_spawned = 0
spawn_rate = 100
frame_count = 0
game_over = False
done = False
L_R = ('left','right')

while not done:
    # --- Main Event Loop ---
    for event in pygame.event.get():                                                # Constantly Checks if the game is being exited
        if event.type == pygame.QUIT:
            done = True

    # --- Keyboard Input ---
        #elif event.type

        elif event.type == pygame.KEYDOWN:
                # --- Pressed Left Button---
                if event.key == pygame.K_LEFT:
                    if player.move(pygame.K_LEFT) == True:
                        if player.moveLimit(pygame.K_LEFT, player_sprite) == True:  # Check if its point is on screen
                            player_sprite.rect.x -= player_sprite.rect.width        # Move 100 px left
                    elif player.move(pygame.K_LEFT)!= False:                        # Else
                        player_sprite.direction(player)                             # Change Sprite Direction
                # --- Pressed Right Button ---
                elif event.key == pygame.K_RIGHT:
                    if player.move(pygame.K_RIGHT) == True:
                        if player.moveLimit(pygame.K_RIGHT, player_sprite) == True: # Check if its point is on screen
                            player_sprite.rect.x += player_sprite.rect.width        # Move 100 px right
                    elif player.move(pygame.K_RIGHT)!= False:                       # Else
                        player_sprite.direction(player)                             # Change Sprite Direction
                # --- Pressed Space Button  ---
                elif event.key == pygame.K_SPACE:                                   # Pressed Spacebar
                    if bullet_count > 0:
                        if player.direction == 'left':
                            bullet = Bullet('left')                                 # Creates a bullet
                            bullet.rect.x = player_sprite.rect.x                    # Bullet x pos = player x pos
                            bullet.rect.y = (player_sprite.rect.y + 33)             # Bullet y pos = player y pos + 33 px to line it up to the gun
                            all_sprites_list.add(bullet)                            # Add the bullet sprite to sprite list
                            bullet_list.add(bullet)                                 # Add bullet to bullet list
                        elif player.direction == 'right':
                            bullet = Bullet('right')                                # Creates a bullet
                            bullet.rect.x = (player_sprite.rect.x + 80)             # Bullet x pos = player x pos + 80 px to line it up to the gun
                            bullet.rect.y = (player_sprite.rect.y + 33)             # Bullet y pos = player y pos + 33 px to line it up to the gun
                            all_sprites_list.add(bullet)                            # Add the bullet sprite to sprite list
                            bullet_list.add(bullet)                                 # Add bullet to bullet list
                    elif bullet_count == 0:
                        game_over == True
                elif event.key == pygame.K_DOWN:
                    game_over = True


        if frame_count % spawn_rate == 0:
            variable = random.choice(L_R)
            zombie = Zombie(variable)
            if variable == 'left':
                zombie.rect.x = 0
            elif variable == 'right':
                zombie.rect.x = 1600
            zombie.rect.y = player_sprite.rect.y
            all_sprites_list.add(zombie)
            zombie_list.add(zombie)
        frame_count += 10

        if game_over == True:
            done = True

    # --- On Screen Text ---

    score_font = pygame.font.SysFont('Calibri', 30, True, False)
    font = pygame.font.SysFont('Calibri', 150, True, False)
    score_text = score_font.render("Score: " + str(score), True, (255,255,255))


    # --- Game Logic ---

    all_sprites_list.update()

    screen.blit(background_image,[0,0])
    screen.blit(score_text, [30, 50])

    all_sprites_list.draw(screen)

    pygame.display.flip()

    for bullet in bullet_list:
        zombie_hit_list = pygame.sprite.spritecollide(bullet, zombie_list, True)

        for zombie in zombie_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 100

        if bullet.rect.x < 0 or bullet.rect.x > 1600:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    for zombie in zombie_list:
        if pygame.sprite.collide_rect(player_sprite, zombie):
            over_text = font.render("Game Over", True, (255,255,255))
            screen.blit(over_text, (500,400))
            pygame.display.flip()
            game_over = True
            pygame.time.delay(1000)
            break








    # Close the window and quit.
pygame.quit()
