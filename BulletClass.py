import pygame

class Bullet:
    def __init__(self):
        self.image=pygame.Surface([4, 10])     #look at player class init and use the same format, no call to a view (recntangle)
        self.image.fill(BLACK)                  #that is all frontend
        self.rect = self.image.get_rect()
        self.rect.x=player.rect.x
        self.rect.y=player.rect.y

    def update(self):
        #code to update state
    
    #ammo function is good
    def ammo(self):
        bullet_list=pygame.sprite.Group()  
        if kill == False:
            bullet_list-=1
        elif kill==True:
            bullet_list.add(bullet)
        return bullet_list

    def shoot(self,bullet,zombie):
        for event in pygame.event.get():                #no user input neccesary
            if event.type = True                        #look at player class as example to structure this code
                update(self)
                if event.key= False
                    bullet.forward(5)
#Here down is good
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
