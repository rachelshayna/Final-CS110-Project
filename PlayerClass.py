import pygame

class PlayerClass():
    def __init__(self):
        self.direction = 'left'


    def move(self, keypress):
        if keypress == pygame.K_LEFT:
            if self.direction == 'left':
                return True
            if self.direction == 'right':
                self.direction = 'left'
                return False
        if keypress == pygame.K_RIGHT:
            if self.direction == 'right':
                return True
            if self.direction == 'left':
                self.direction = 'right'
                return False
    def moveLimit(self, keypress, player):
        if keypress == pygame.K_LEFT:
            if player.rect.x >= 100:
                return True
            else:
                return False
        elif keypress == pygame.K_RIGHT:
            if player.rect.x <= 1400:
                return True
            else:
                return False
    def direction(self):
        return(self.direction)
#end game
    def death(self,zombie):
        if self.rect.colliderect(zombie.rect):
            return True
        elif Bullet.ammo ==0:
            return True
        else:
            return False
