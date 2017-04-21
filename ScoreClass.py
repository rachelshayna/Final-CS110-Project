import time
import pygame

class Score:
    def __init__(self,xcor,ycor,time):
        self.xcor=xcor
        self.ycor=ycor
        self.time=time

    def killZombie(self,zombie,bullet):
        if pygame.sprite.spritecollide(bullet, zombie, True):
            player.score+=1
        return player.score

    def survivalTime(self):
        clock=pygame.time.Clock()
        """sec=0
        rate=60
        total_seconds=sec//rate
        minutes=total_seconds//60
        seconds=total_seconds%60
        time_string="Time: {0:02}:{1:02}".format(minutes,seconds)
        text=font.render(time_string,True,BLACK)
        screen.blit(text,[250,250])"""
        while player.death == False:
            return pygame.time.get_ticks()
        if player.death==True:
            pygame.time.wait()
            return pygame.time.get_ticks()

        #writing to a file --> for data requirement
#Won't need an x and y coordinate, but would be handled by your view
#This should keep track of time and high scores of how long people could stay alive
