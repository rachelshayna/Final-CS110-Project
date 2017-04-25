import pygame
import sys

class Game:
    def __init__(self):
        self.done=False
        self.fps=60
        self.screen=pg.display.set_mode((1280,720))
        self.screen_rect=self.screen.get_rect()
        self.clock=pg.time.Clock()
        self.spawn_timer=0
        self.spawn_frequency=3000
        self.zombies=pg.sprite.Group()

    def event_loop(self):
        while self.done is False:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    self.done=True
                elif player.death is True:
                    self.done=True

    def update(self):
        time_passed=0
        zombie_list=0
        time_passed+=clock.tick(60)
        if time_passed>=500:
            time_passed=0
            zombie_list+=1
        if self.spawn_timer>=self.spawn_frequency:
            random.choice(Zombie(<parameters>).spawnLeft(),Zombie(<parameters>).spawnRight())
            self.spawn_timer-=self.spawn_frequency
            Zombie(self.screen_rect.center,self.zombies)
        #self.zombies.update(dt)
        #just check time

    def run(self):
        while not self.done:
            dt=self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            pg.display.update()
