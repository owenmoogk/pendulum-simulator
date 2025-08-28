import pygame
import settings
from pendulum import Pendulum
from drawWindow import drawWindow
import matplotlib.pyplot as plt
import graphing

# globals
clock = pygame.time.Clock()
pendulum = Pendulum()
plt.ion()
graphing.initGraph()
timeElapsed = 0

def main():
    
    while True:
        deltaTime = 30 / 1000 # seconds
        global timeElapsed 
        timeElapsed += deltaTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.VIDEORESIZE:
                settings.windowHeight = pygame.display.get_surface().get_height()
                settings.windowWidth = pygame.display.get_surface().get_width()

                pendulum.dimensionChange()

        pendulum.update(deltaTime)
        drawWindow(settings.screen, pendulum)

        graphing.logData(pendulum, timeElapsed)

        graphing.updateGraph()

if __name__ == "__main__":
    main()