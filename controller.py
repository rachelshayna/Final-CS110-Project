import pygame
import random                                                                   # Q: Why can't you take an atom seriously?
from PlayerClass import PlayerClass                                             # A: Because they make up everything!
from view_Player import view_Player
from Zombie import Zombie
from Bullet import Bullet


class controller:
    def __init__(self):
        self.score = 0
        self.highscore(self.score)

    def start(self):
        screen = pygame.display.set_mode((1600,900))
        pygame.display.set_caption('Zombie Apocalypse')


        ready = False
        while ready == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True
                start_image = pygame.image.load("game_start.png").convert()
                screen.blit(start_image,[0,0])
                pygame.display.flip()


    def play(self):
        screen = pygame.display.set_mode((1600,900))
        pygame.display.set_caption('Zombie Apocalypse')
        clock = pygame.time.Clock()
        BLACK = (0, 0, 0)
        L_R = ('left','right')


        background_image = pygame.image.load("background.png").convert()

        # --- Sprite Lists ---
        all_sprites_list = pygame.sprite.Group()
        zombie_list = pygame.sprite.Group()
        bullet_list = pygame.sprite.Group()

        # --- Create Player Sprite ---
        player_sprite = view_Player(800, 600)
        player = PlayerClass()
        all_sprites_list.add(player_sprite)

        dead = False
        bullet_count = 10
        zombie_spawned = 0
        spawn_rate = 100
        frame_count = 0


        while not dead:
            # --- Main Event Loop ---
            for event in pygame.event.get():                                                # Constantly Checks if the game is being exited
                if event.type == pygame.QUIT:
                    dead = True

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
                                    bullet_count -= 1
                                elif player.direction == 'right':
                                    bullet = Bullet('right')                                # Creates a bullet
                                    bullet.rect.x = (player_sprite.rect.x + 80)             # Bullet x pos = player x pos + 80 px to line it up to the gun
                                    bullet.rect.y = (player_sprite.rect.y + 33)             # Bullet y pos = player y pos + 33 px to line it up to the gun
                                    all_sprites_list.add(bullet)                            # Add the bullet sprite to sprite list
                                    bullet_list.add(bullet)                                 # Add bullet to bullet list
                                    bullet_count -= 1
                elif bullet_count == 0:
                    dead = True


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



            # --- On Screen Text ---

            score_font = pygame.font.SysFont('Calibri', 30, True, False)
            font = pygame.font.SysFont('Calibri', 150, True, False)
            score_text = score_font.render("Score: " + str(self.score), True, (255,255,255))
            bullet_text = score_font.render("Bullet: " + str(bullet_count), True, (255,255,255))


            # --- Game Logic ---

            all_sprites_list.update()

            screen.blit(background_image,[0,0])
            screen.blit(score_text, [30, 50])
            screen.blit(bullet_text, [1400, 50])

            all_sprites_list.draw(screen)

            pygame.display.flip()

            for bullet in bullet_list:
                zombie_hit_list = pygame.sprite.spritecollide(bullet, zombie_list, True)

                for zombie in zombie_hit_list:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                    self.score += 100
                    bullet_count += 1

                if bullet.rect.x < 0 or bullet.rect.x > 1600:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)

            for zombie in zombie_list:
                if pygame.sprite.collide_rect(player_sprite, zombie):
                    dead = True


    def end(self):
        screen = pygame.display.set_mode((1600,900))
        pygame.display.set_caption('Zombie Apocalypse')
        clock = pygame.time.Clock()
        ready = False
        while ready == False:
            end_image = pygame.image.load("game_over.png").convert()
            screen.blit(end_image,[0,0])
            write_score = self.highscore(self.score)
            font = pygame.font.SysFont('Calibri', 70, True, False)
            hi_score = font.render("High Score: " + str(write_score), True, (255,255,255))
            screen.blit(hi_score, (600, 500))
            pygame.display.flip()
            self.score = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True

    def highscore(self, score):
      infile = open("hiscore.txt", "r")
      old_hi = int(infile.readline())
      infile.close()
      outfile = open("hiscore.txt", "w")
      if old_hi > score:
        outfile.write(str(old_hi))
        return old_hi
      outfile.write(str(score))
      return score
