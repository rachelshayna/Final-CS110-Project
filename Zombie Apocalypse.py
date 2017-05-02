import pygame                                                      # Henry Chen
import random                                                      # Q: Why can't you take an atom seriously?
import PlayerClass                                                 # A: Because they make up everything!
import view_Player
import Zombie
import Bullet
from controller import controller

def main():
    pygame.init()

    game = controller()

    if game.start() == True:
        game.play()
        while game.end() == True:
            game.play()
    pygame.quit()

main()
