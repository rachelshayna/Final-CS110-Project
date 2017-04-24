import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image=''
        self.score=0
        self.change_x=0
        self.change_y=0

    def __str__(self):
        string=""
        string+="X Coordinate: "+str(self.xcor)+"\n"
        string+="Y Coordinate: "+str(self.ycor)+"\n"
        return string

    def changespeed(self,x,y):
        self.change_x+=x
        

    def update(self,x,y):
        self.rect.x+=self.change_x
        self.rect.y+=self.change_y

    def collision(self,zombie):
        return self.rect.colliderect(zombie.rect)

    def death(self,zombie):
        if self.colliderect(zombie):
            del self
            return True
        elif Bullet.ammo ==0:
            del self
            return True
        else:
            return False

        """if collision == True:
                del player"""
