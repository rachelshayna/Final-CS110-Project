import pygame
import time
import random

class Zombies:
    def __init__(self,x,speed):
        self.x=x
        self.y=0
        self.image=pygame.image.load("""Image File""")
        self.rect=pygame.image.get_rect()
        self.speed=speed
        zombies_group=[]

    def movement(self):
        self.rect=self.rect.move(self.speed)

#spawn zombie left
    def spawnLeft(self):
        zombies_group.append(Zombies,<ScreenSizeLeft>)

#spawn zombie right
    def spawnRight(self):
        zombies_group.append(Zombies,<ScreenSizeRight>)
        
#zombies spawn randomly on left and right at increasing intervals
    def Spawn(self,zombie):
        while player.death == False:
            instance=1
            faster=1
            if score.survivalTime!=0:
                random.choice(spawnLeft, spawnRight)*faster
                instance+=1
                if instance==5:
                    instance=1
                    faster+=1
                    

#if spawn on left, go right
    def update(self):
        for zombie in zombies_group:
            if zombie.spawnLeft:
                zombie.changespeed(3,0)
            elif zombie.spawnRight:
                zombie.changespeed(-3,0)

#zombie dies
    def death(self,bullet):
        if self.rect.colliderect(bullet.rect):
            zombies_group.remove()
