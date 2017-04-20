import time
import random
#import pygame
import threading

class Zombies:
	def __init__(self, xcor, ycor):
		self.xcor = xcor
		self.ycor= ycor
	def __str__(self):
		string = ""
		string += "X Coordinate: " + str(self.xcor) + "\n"
		string += "Y Coordinate: " + str(self.ycor) + "\n"
		return string
	def movement(self):
		xvar=player.xcor
		yvar=player.ycor
		self.movement(xvar,yvar)
	def death(self , bullet):
		if self.xcor == bullet.xcor:
			return("Zombie's Dead")
		else: return "Alive!"

class Spawn:
	def __init__(self,xcor,ycor):
		self.xcor=xcor
		self.ycor=ycor
	def zspawn(self):
		zombies=0
		self.zombies=threading.Timer(3, zombies.movement()).start()

class Player:

	def __init__(self,xcor,ycor):
		self.xcor=xcor
		self.ycor=ycor
	def __str__(self):
		string = ""
		string += "X Coordinate: " + str(self.xcor) + "\n"
		string += "Y Coordinate: " + str(self.ycor) + "\n"
		return string
	def movement(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor
	def death(self, zombie):
		if self.xcor == zombie.xcor :
		 	return ("game_over")

class Score:
	def __init__(self, xcor, ycor, time):
		self.xcor=xcor
		self.ycor=ycor
		self.time=time

class Bullet:
	def __init__(self, xcor, ycor):
		self.xcor=xcor
		self.ycor=ycor
		#self.bulletcount=bulletcount

	def movement(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor

	def hit(self, bullet, zombie):
		if bullet.xcor==zombie.xcor :
			return("delete zombie")
		else:
			return("delete bullet")
