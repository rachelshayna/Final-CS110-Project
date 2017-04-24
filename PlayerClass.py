import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image=''
        self.score=0
        self.change_x=0

    def __str__(self):
        string=""
        string+="X Coordinate: "+str(self.xcor)+"\n"
        return string

    def move(self,x):
        if k_down = left:
            self.change_x-=x
        elif k_down = right:
            self.change_x +=x
        
    def update(self,x):
        self.rect.x+=self.change_x

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
