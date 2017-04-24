import time
import pygame

class Score:
    def __init__(self,xcor,ycor,time):
        self.xcor=xcor
        self.ycor=ycor
        self.time=time

    def killZombie(self,zombie,bullet):
        if pygame.sprite.spritecollide(bullet, zombie, True):
            player.score+=1
        return player.score

    def survivalTime(self):
        clock=pygame.time.Clock()
        while player.death == False:
            return pygame.time.get_ticks()
        if player.death==True:
            pygame.time.wait()
            return pygame.time.get_ticks()
