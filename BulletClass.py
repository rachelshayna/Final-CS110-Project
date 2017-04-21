import pygame

class Bullet:
    def __init__(self):
        self.image=pygame.Surface([4, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=player.rect.x
        self.rect.y=player.rect.y

    def ammo(self):
        bullet_list=pygame.sprite.Group()
        if kill == False:
            bullet_list-=1
        elif kill==True:
            bullet_list.add(bullet)
        return bullet_list

    def shoot(self,bullet,zombie):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    bullet.forward(5)

    def hit (self,zombie):
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
