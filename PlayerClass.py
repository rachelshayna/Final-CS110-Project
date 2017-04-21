import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        self.image=''
        self.score=0
        self.screenSize=(640,480)
        self.screen=pygame.display.set_mode(self.screenSize)
        self.change_x=0
        self.change_y=0


    def __str__(self):
        string=""
        string+="X Coordinate: "+str(self.xcor)+"\n"
        string+="Y Coordinate: "+str(self.ycor)+"\n"
        return string

    def changespeed(self,x,y):
        self.change_x+=y
        self.change_y+=y

    def update(self):
        self.rect.x+=self.change_x
        self.rect.y+=self.change_y

    def movement(self,xcor,ycor):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    player.changespeed(-3,0)
                if event.key==pygame.K_RIGHT:
                    player.changespeed(3,0)
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    player.changespeed(3,0)
                if event.key==pygame.K_RIGHT:
                    player.changespeed(-3,0)


    def collision(self,zombie):
        return self.rect.colliderect(zombie.rect)

    def death(self,zombie):
        if self.colliderect(zombie):
            del self
        elif Bullet.ammo ==0:
            del self

        """if collision == True:
                del player"""
