import time
import random
import pygame
import threading

class Player:
    def __init__(self,xcor,ycor):
        self.xcor=xcor
        self.ycor=ycor
        self.image=''

    def __str__(self):
        string=""
        string+="X Coordinate: "+str(self.xcor)+"\n"
        string+="Y Coordinate: "+str(self.ycor)+"\n"
        return string

    def movement(self,xcor,ycor):
        self.xcor=xcor
        self.ycor=ycor
        #send in a direction, not an x and y coordinate. Moving one or two pixel at a time.

    def death(self,zombie):
        if self.xcor==zombie.xcor:
            return ("game_over")
        """return self.rect.colliderect(sprite.rect)"""
