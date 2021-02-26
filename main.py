# INIT
import pygame, time
from settings import *
from pendulum import *
from math import sin
from drawWindow import *

# globals
clock = pygame.time.Clock()
pendulum = Pendulum()

while True:
    clock.tick(simSpeed)

    # quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pendulum.update()
    drawWindow(screen, pendulum)