import pygame
import time

class Zombie:
    def __init__(self,x,speed):
        self.x=x
        self.y=0
        self.image=pygame.image.load("""Image File""")
        self.rect=pygame.image.get_rect()
        self.speed=speed
        alive_zombies=zombies.sprites()
        zombie_group=[zombie for zombie in zombies if bullet.kill()==False]

    def movement(self):
        self.rect=self.rect.move(self.speed)

#spawn zombie left
    def spawnLeft(self):
        zombie_group.append(Zombie,<ScreenSizeLeft>) #might need to append tuple
        update()

#spawn zombie right
    def spawnRight(self):
        zombie_group.append(Zombie,<ScreenSizeRight>)
        update()

#if spawn on left, go right
    def update(self):
        for zombie in zombie_group:
            if zombie.spawnLeft:
                zombie.changespeed(3,0)
            elif zombie.spawnRight:
                zombie.changespeed(-3,0)

#zombie dies
    def death(self,bullet):
        if self.rect.colliderect(bullet.rect):
            zombie_group.remove(self) #or self.remove()
            score.killZombie()

