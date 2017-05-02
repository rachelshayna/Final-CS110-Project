import pygame
from PlayerClass import PlayerClass


class view_Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image = pygame.image.load("player_left.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def direction(self, player):
        if player.direction == 'left':
            self.image = pygame.image.load("player_left.png").convert_alpha()
        elif player.direction == 'right':
            self.image = pygame.image.load("player_right.png").convert_alpha()
