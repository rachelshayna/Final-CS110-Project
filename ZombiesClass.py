import time
import random
import pygame
import threading

class Zombies:
    def __init__(self,xcor,ycor):
        self.xcor=xcor
        self.ycor=ycor
        self.image='' #ADD WITH PYGAME

    def __str__(self):
        string=""
        string+="X Coordinate: " + str(self.xcor) + "\n"
        string+="Y Coordinate: " + str(self.ycor) + "\n"
        return string

    def movement(self):
        xvar=player.xcor
        yvar=player.ycor
        self.movement(xvar,yvar)

    def death(self,bullet):
        if self.rect.colliderect(bullet.rect):
            del zombie
