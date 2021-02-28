import pygame, time, threading
from settings import *
from pendulum import *
from math import sin
from drawWindow import *
import data
import matplotlib.pyplot as plt
# globals
clock = pygame.time.Clock()
pendulum = Pendulum()


plt.ion()

x = data.data["x"]
y = data.data["y"]

figure, ax = plt.subplots()
line1, = ax.plot(x, y)

def updateGraph():
    x = data.data["ticks"]
    y = data.data["angle"]

    line1.set_xdata(x)
    line1.set_ydata(y)
    ax.margins(1000)

    figure.canvas.draw()
    figure.canvas.flush_events()

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
        updateGraph()
        drawWindow(screen, pendulum)
        data.data["x"].append(pendulum.nodeX - pendulum.originX)
        data.data["y"].append(-(pendulum.nodeY - pendulum.originY))
        data.data["ticks"].append(tick)
        data.data["angle"].append(pendulum.angle)

main()