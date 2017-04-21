import BulletClass
import ControllerClass
import PlayerClass
import ScoreClass
import SpriteClass
import Zombies Class 
import pygame
import random 
import time 
import threading 

def __str__(self):
        string=""
        string+="X Coordinate: " + str(self.xcor) + "\n"
        string+="Y Coordinate: " + str(self.ycor) + "\n"
return string

def main(): 
	#BulletClass() 
	#ControllerClass()
	#PlayerClass()
	#ScoreClass()
	#SpriteClass()
	'''what is the sprite class doing?'''
	#Zombies Class()
	
	Z1= ZombieClass.Zombies(10,10)
	#print(Z1)
	P = PlayerClass.Player(5,5)
	P.movement(10,10)
	print(P.death(Z1))
	Zombie.__str___(Zombie) #is this the right formatting? Also aren't we supposed to avoid str functions?  
	
	Z2 = ZombieClass.Zombies(11,11)
	#print(Z2)
	B = BulletClass.Bullet(17,17)
	B.movement(11,11)
	print(Z2.death(B))
	print(B.hit(B, Z2))

	print(ScoreClass.Score())

	

main()
	
