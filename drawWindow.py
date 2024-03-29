import settings
from settings import black, gravity, mass, backgroundColor, myFont
from math import degrees
import pygame

def drawWindow(screen, pendulum):
    screen.fill(backgroundColor)
    pendulum.draw()

    # labels
    score_label = myFont.render("Angle: " + str(round(degrees(pendulum.angle), 4)),1,black)
    screen.blit(score_label, (10, 10))
    score_label = myFont.render("Acceleration: " + str(round(pendulum.angularAcceleration*100, 4)),1,black)
    screen.blit(score_label, (10, 40))
    score_label = myFont.render("Velocity: " + str(round(pendulum.angularVelocity*100, 4)),1,black)
    screen.blit(score_label, (10, 70))
    score_label = myFont.render("Mass: " + str(mass),1,black)
    screen.blit(score_label, (10, settings.windowHeight-40))
    score_label = myFont.render("Gravity: " + str(gravity),1,black)
    screen.blit(score_label, (10, settings.windowHeight-70))

    pygame.display.update()