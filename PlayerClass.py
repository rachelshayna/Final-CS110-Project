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

#find what direction player is facing
    def direction(self,x,y):
        

#end game
    def death(self,zombie):
        if self.rect.colliderect(zombie.rect):
            return True
        elif Bullet.ammo ==0:
            return True
        else:
            return False

#find player direction; boolean value; check BV for player and set BV of the bullet ; then check bullets fired in event loop; if not empty, keep moving in whatever direction its facing; removed only if it one-hits a zombie or is outside window 
