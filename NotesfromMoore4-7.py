import time
import random
#import pygame
import threading

'''
Start with the person in an empty room with zombies coming at them. The maze, is part of the "nice to have" section, but not pertinent.
'''


class Zombies:
	def __init__(self, xcor, ycor):
		self.xcor = xcor
		self.ycor= ycor
		self.image = ''
#the above empty string will eventually be part of a pygame module
	def __str__(self):
		string = ""
		string += "X Coordinate: " + str(self.xcor) + "\n"
		string += "Y Coordinate: " + str(self.ycor) + "\n"
		return string
	def movement(self):
		xvar=player.xcor
		yvar=player.ycor
		self.movement(xvar,yvar)
'''
Pass an x,y unit as to where the player is. Then the zombie has to move a unit at a time to be constantly moving towards the player. Figure out the x coordinate (if < or >, add or subtract 1 accordingly)
'''
	def death(self , bullet):
		if self.xcor == bullet.xcor and self.ycor == bullet.ycor:
			return("Zombie's Dead")
#when we start using pygame, there's a collision ability which will be used instead of this
		else: 
			return "Alive!"
#At some point we're going to need to keep track of the zombies as images, since they're stored as x and y. This is something we'll learn after break but we should add a tentative part of the init that the self.image (to keep track of data items)


class Spawn:
#this class should be a function in the Controller class 
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
		self.image #this is like the zombie note above 
	def __str__(self):
		string = ""
		string += "X Coordinate: " + str(self.xcor) + "\n"
		string += "Y Coordinate: " + str(self.ycor) + "\n"
		return string
	def movement(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor
#send in a direction, not an x and y coordinate. Moving one or two pixel at a time. 
	def death(self, zombie):
		if self.xcor == zombie.xcor :
		 	return ("game_over")
#same collision note as above 

class Score:
	def __init__(self, xcor, ycor, time):
		self.xcor=xcor
		self.ycor=ycor
		self.time=time
#writing to a file --> for data requirement 
#Won't need an x and y coordinate, but would be handled by your view
#This should keep track of time and high scores of how long people could stay alive 

class Bullet:
	def __init__(self, xcor, ycor):
		self.xcor=xcor
		self.ycor=ycor
		#self.bulletcount=bulletcount

	def movement(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor
#same deal as above
#pass in parameter direction so it moves in that direction forever until it hits something or leaves the screen. DOn't need the x and y coor because you just need the initial direction
#loop
	def hit(self, bullet, zombie):
		if bullet.xcor==zombie.xcor :
			return("delete zombie")
		else:
			return("delete bullet")
#collision stuff from pygame but good for now 

'''Each of these class should be on a different file'''
