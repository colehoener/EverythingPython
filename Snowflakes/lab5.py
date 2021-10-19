import pygame
import sys
from Drawable import Drawable
from Rectangle import Rectangle
from Snowflake import Snowflake
import random

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snowflakes')

#colors
BLUE = (  3,   155, 229)
GREEN = (  67, 160,   71)

snowflakes = []

toggle = False
while True: # main game loop

    sky = Rectangle(0, 0, 800, 400, BLUE)
    sky.draw(DISPLAYSURF)

    ground = Rectangle(0, 400, 800, 200, GREEN)
    ground.draw(DISPLAYSURF)


    for j in snowflakes:
        j.draw(DISPLAYSURF)
        x, y = j.getLoc()
        if j.getMaxY() > y and toggle == True:
            j.incrY()

    if toggle == True:
            snowflakes.append(Snowflake(random.randint(0,800), 0, random.randint(400, 600)))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[pygame.K_q]):
            print('Trying to quit')
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            toggle = not toggle
        
        

    pygame.display.update() 