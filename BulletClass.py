import pygame

class Bullet:
    def __init__(self):
        self.image=''
        self.change_x=0
        self.change_y=0

    def changespeed(self,x):
        self.change_x+=x

    def update(self,x):
        self.rect.x+=self.change_x

    def ammo(self):
        bullet_list=pygame.sprite.Group()
        if shoot==True:
            if kill==True:
                bullet_list.add(bullet)
            else:
                bullet_list-=1
        return bullet_list

    def shoot(self,bullet):
        bullet.forward(5)
        update(self)

    def hit (self,zombie):
        if shoot==True:
            for bullet in bullet_list:
                killedzombies=pygame.sprite.spritecollide(bullet, zombie, True)
                for zombie in killedzombies:
                    bullet_list.remove(bullet)
        return self.rect.colliderect(zombie.rect)

    def kill(self,zombie):
        if hit==True:
            del zombie
            del bullet
        else:
            del bullet
