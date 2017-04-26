import pygame

class Bullet:
    def __init__(self):
        self.image=''
        self.change_x=0
        self.change_y=0
        bullet_list=pygame.sprite.Group()
        killed_zombies=pygame.sprite.spritecollide(bullet, zombie, True)

    def changespeed(self,x):
        self.change_x+=x

    def update(self,x):
        self.rect.x+=self.change_x
        for zombies in killed_zombies:
            zombie.death()
        if bullet.rect.x >= 1600 or bullet.x <= 0:
            bullet.remove(bullet)

    def ammo(self):
        if shoot==True:
            if kill==True:
                bullet_list.add(bullet)
            else:
                bullet_list-=1
        return bullet_list

    def direction(self):
        if bullet.shoot() is True:
            if player.direction==True:
                zombie.changespeed(-3,0)
            elif player.direction==False:
                zombie.changespeed(3,0)
        
    def shoot(self):
        bullet.forward(100)
        update(self)
        return True

    def kill(self,zombie):
        if bullet.shoot() is True:
            for bullet in bullet_list:
                if self.rect.colliderect(zombie.rect)==True:
                    del bullet
                    bullet_list.add(bullet)
                else:
                    del bullet
                    bulletlist.remove(bullet)
