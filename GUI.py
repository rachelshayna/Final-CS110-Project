import pygame
import sys
from PlayerClass import PlayerClass
import view_Background
from view_Player import view_Player

pygame.init()

clock = pygame.time.Clock() #Used to manage how fast the screen updates

screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('Zombie Apocalypse')

background_position = [0,0]
background_image = pygame.image.load("background.png").convert()


player_sprite = view_Player(800, 600)
player = PlayerClass()

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player_sprite)

game_over = False
done = False

while not done:
    # --- Main Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Keyboard Input ---
        elif event.type == pygame.KEYDOWN:
                # --- Pressed Left Button---
                if event.key == pygame.K_LEFT:
                    if player.move(pygame.K_LEFT) == True:                          # Move Left
                        if player.moveLimit(pygame.K_LEFT, player_sprite) == True:  # Check if its point is on screen
                            player_sprite.rect.x -= player_sprite.rect.width        # Move 100 px left
                    elif player.move(pygame.K_LEFT)!= False:                        # Else
                        player_sprite.direction(player)                             # Change Sprite Direction
                # --- Pressed Right Button ---
                elif event.key == pygame.K_RIGHT:
                    if player.move(pygame.K_RIGHT) == True:                         # Move Right
                        if player.moveLimit(pygame.K_RIGHT, player_sprite) == True: # Check if its point is on screen
                            player_sprite.rect.x += player_sprite.rect.width        # Move 100 px right
                    elif player.move(pygame.K_RIGHT)!= False:                       # Else
                        player_sprite.direction(player)                             # Change Sprite Direction

                #elif event.key == pygame.K_SPACE:
                    #player class code: Fires a bullet

        #elif event.type == #player alive = 0
        #    game_over = True
    screen.blit(background_image,[0,0])

    all_sprites_list.draw(screen)

    pygame.display.flip()
    # Close the window and quit.
pygame.quit()
