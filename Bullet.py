import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.direction = direction

    def update(self):
        if self.direction == 'left':
            self.rect.x -= 50
        elif self.direction == 'right':
            self.rect.x += 50
