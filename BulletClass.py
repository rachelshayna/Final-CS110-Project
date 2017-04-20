import time
import random
import pygame
import threading

class Bullet:
    def __init__(self,xcor,ycor):
        self.xcor=xcor
        self.ycor=ycor

    def movement(self,xcor,ycor):
        self.xcor=xcor
        self.ycor=ycor
  #      send in a direction, not an x and y coordinate. Moving one or two pixel at a time.
  #pass in parameter direction so it moves in that direction forever until it hits something or leaves the screen. DOn't need the x and y coor because you just need the initial direction
#loop
    def hit(self,bullet,zombie):
        if bullet.xcor==zombie.xcor:
            return("delete zombie")
        else:
            return("delete bullet")
        """ return self.rect.colliderect(sprite.rect)"""
