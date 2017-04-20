import time
import random
import pygame
import threading

class Score:
    def __init__(self,xcor,ycor,time):
        self.xcor=xcor
        self.ycor=ycor
        self.time=time
        #writing to a file --> for data requirement 
#Won't need an x and y coordinate, but would be handled by your view
#This should keep track of time and high scores of how long people could stay alive 
