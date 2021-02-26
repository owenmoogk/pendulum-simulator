from settings import *
from math import sin, cos
import pygame

class Pendulum:
    def __init__(self):

        self.originX = windowWidth / 2
        self.originY = 100
        self.originColor = grey
        self.originRadius = 10

        self.nodeX = length * sin(initAngle) + self.originX
        self.nodeY = length * cos(initAngle) + self.originY
        self.nodeColor = red
        self.nodeRadius = 40

        self.angularAcceleration = 0
        self.angularVelocity = 0
        self.angle = initAngle

    def update(self):
        self.angularAcceleration = -movementConstant * sin(self.angle) / length
        self.angularVelocity += self.angularAcceleration
        self.angularVelocity *= dampening
        self.angle += self.angularVelocity

        self.nodeX = length * sin(self.angle) + self.originX
        self.nodeY = length * cos(self.angle) + self.originY

    def draw(self):
        pygame.draw.line(screen, pink, (self.originX, self.originY), (self.nodeX, self.nodeY), 3)
        pygame.draw.circle(screen, self.nodeColor, (self.nodeX, self.nodeY), self.nodeRadius)
        pygame.draw.circle(screen, self.originColor, (self.originX, self.originY), self.originRadius)