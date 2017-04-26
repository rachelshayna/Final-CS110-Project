import pygame
import time

class Zombie:
    def __init__(self,x, speed):
        self.x = x
        self.speed=speed
        alive_zombies=zombies.sprites()
        zombie_group=[zombie for zombie in zombies if bullet.kill()==False]

    def rightmovement(self):
        zombie.rect.x += zombie.rect.width
    
    def leftmovement(self):
        zombie.rect.x -= zombie.rect.width

    def spawn:
        if clock.tick(gametime) == clock.tick(time):
            if random.randchoice(2) == 0:
                self.spawnLeft()
            elif random.randchoice(2) == 1:
                self.spawnRight()
                      
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
    def death(self, bullet):
        if self.rect.colliderect(bullet.rect):
            self.remove() #or self.remove()
            zombie_sprite.remove()
                #update score

