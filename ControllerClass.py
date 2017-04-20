import time
import random
import pygame
import threading

class Controller:
    def __init__(self,xcor,ycor,zombie):
        self.xcor=xcor
        self.ycor=ycor
        zombies=0
        self.zombies=threading.Timer(3,zombies.movement()).start()

    def Spawn(self):
        #work on this
