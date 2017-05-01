import pygame

class Zombie(pygame.sprite.Sprite):
    def __init__(self, direction):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([4, 10])
        if direction == 'left':
            self.image = pygame.image.load('zombie_right.png').convert_alpha()
        elif direction == 'right':
            self.image = pygame.image.load('zombie_left.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.direction = direction


    def update(self):
        if self.direction == 'left':
            self.rect.x += 50
        elif self.direction == 'right':
            self.rect.x -= 50
