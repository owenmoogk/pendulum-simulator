import pygame, time, threading
from settings import *
from pendulum import *
from math import sin
from drawWindow import *
import data
import matplotlib.pyplot as plt
from graphing import *

# globals
clock = pygame.time.Clock()
pendulum = Pendulum()
plt.ion()
initGraph()

def main():
    tick = 0
    while True:
        tick += 1
        clock.tick(simSpeed)

        # quit function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data.running = False
                pygame.quit()

        pendulum.update()
        drawWindow(screen, pendulum)

        data.data["x"].append(pendulum.nodeX - pendulum.originX)
        data.data["y"].append(-(pendulum.nodeY - pendulum.originY))
        data.data["ticks"].append(tick)
        data.data["angle"].append(pendulum.angle)
        data.data["velocity"].append(pendulum.angularVelocity)
        data.data["acceleration"].append(pendulum.angularAcceleration)
        # # pe = mgh (height is referenced from the lowest point)
        # data.data["potential"].append(mass * gravity * (pendulum.originY+length - pendulum.nodeY))
        # data.data["kinetic"].append(0.5 * mass * (pendulum.angularVelocity**2))

        updateGraph(tick)

if __name__ == "__main__":
    main()