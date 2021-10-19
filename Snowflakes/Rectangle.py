from Drawable import Drawable
import pygame, sys
from pygame.locals import *

class Rectangle(Drawable):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        x,y = super().getLoc()
        pygame.draw.rect(surface , self.color, (x, y, self.width, self.height))
        #pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
    