import pygame
import time

class Zombie:
    def __init__(self,x,speed):
        self.x=x
        self.y=0
        self.image=pygame.image.load("""Image File""")
        self.rect=pygame.image.get_rect()
        self.speed=speed
        zombie_group=[zombie for zombie in zombies if bullet.kill()==False]
        clock=pygame.time.Clock()

    def movement(self):
        self.rect=self.rect.move(self.speed)

#spawn zombie left
    def spawnLeft(self):
        zombie_group.append(self.__init__) #might need to append tuple
        update()
        return True

#spawn zombie right
    def spawnRight(self):
        zombie_group.append(self.__init__)
        update()
        return True

    def spawnRate(self):
        time_passed+=clock.tick(1000)
        rate=10000
        if time_passed>=rate:
            time_passed=0
            zombie_group+=1    
            choice=random.choice(zombie.spawnLeft(), zombie.spawnRight())
            rate-=100
            if choice == zombie.spawnLeft:
                zombie.spawnLeft()
            elif choice==zombie.spawnRight:
                zombie.spawnRight()
            #if rate==100:
                #we'll see how this works 

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
