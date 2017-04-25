import pygame

class Bullet:
    def __init__(self):
        self.image=''
        self.change_x=0
        self.change_y=0
        bullet_list=pygame.sprite.Group()
        killed_zombies=[zombie for zombie in zombies if bullet.kill()==True]
        #OR: killed_zombies=pygame.sprite.spritecollide(bullet, zombie, True)

    def changespeed(self,x):
        self.change_x+=x

    def update(self,x):
        self.rect.x+=self.change_x
        for zombies in killed_zombies:
            zombie.death()
        if bullet.x > <ScreenSizeRight> or bullet.x < <ScreenSizeLeft>:
            bullet.remove(bullet)

    def ammo(self):
        if shoot==True:
            if kill==True:
                bullet_list.add(bullet)
            else:
                bullet_list-=1
        return bullet_list

    def direction(self,bullet):
        return fdf dd
        
    def shoot(self,bullet):
        bullet.forward(5)
        update(self)
        return True

    """def hit (self,zombie):
        if bullet.shoot()==True:
            for bullet in bullet_list:
                for zombie in killedzombies:
                    bullet_list.remove(bullet)
        return self.rect.colliderect(zombie.rect)"""

    def kill(self,zombie):
        if bullet.shoot()==True:
            for bullet in bullet_list:
                if self.rect.colliderect(zombie.rect)==True:
                    del bullet
                    bullet_list.add(bullet)
                else:
                    del bullet
                    bulletlist.remove(bullet)

#find bullet direction

