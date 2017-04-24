import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image=''
        self.score=0
        self.change_x=0
        self.change_y=0

#move player
    def changespeed(self,x):
        self.change_x+=x

    def update(self,x):
        self.rect.x+=self.change_x

#see if player touches zombie
    def collision(self,zombie):
        return self.rect.colliderect(zombie.rect)

#player death
    def death(self,zombie):
        if collision==True:
            del self
            return True
        elif Bullet.ammo ==0:
            del self
            return True
        else:
            return False
