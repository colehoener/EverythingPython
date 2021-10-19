from Drawable import Drawable
import pygame
from pygame.locals import *
import random


class Snowflake(Drawable):
    def __init__(self, x, y = 0, maxY = 0):
        super().__init__(x, y)
        self.maxY = maxY

    def getMaxY(self):
        return self.maxY

    def incrY(self):
        x, y = super().getLoc()
        y += random.randint(1,5)
        super().setLoc([x, y])
    
    def draw(self, surface):
        white = (255, 255, 255)
        x,y = super().getLoc()
        pygame.draw.line(surface, white, (x-5,y), (x+5,y)) 
        pygame.draw.line(surface, white, (x, y-5), (x, y+5)) 
        pygame.draw.line(surface, white, (x-5, y-5), (x+5, y+5)) 
        pygame.draw.line(surface, white, (x-5, y+5), (x+5, y-5)) 