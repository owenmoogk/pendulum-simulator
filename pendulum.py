import settings
from math import sin, cos, degrees, radians
import pygame

class Pendulum:
    def __init__(self):

        self.originX = settings.windowWidth // 2
        self.originY = settings.windowHeight // 2
        self.originColor = settings.grey
        self.originRadius = 10

        self.nodeX = settings.length * sin(settings.initAngle) + self.originX
        self.nodeY = settings.length * cos(settings.initAngle) + self.originY
        self.nodeColor = settings.red
        self.nodeRadius = 40

        self.angularAcceleration = 0
        self.angularVelocity = 0
        self.angle = settings.initAngle

    def update(self):

        self.angularAcceleration = -settings.movementConstant * sin(self.angle) / settings.length
        self.angularVelocity += self.angularAcceleration
        self.angularVelocity *= settings.dampening
        self.angle += self.angularVelocity

        if degrees(self.angle) > 180:
            self.angle -= radians(360)
        if degrees(self.angle) < -180:
            self.angle += radians(360)

        self.nodeX = settings.length * sin(self.angle) + self.originX
        self.nodeY = settings.length * cos(self.angle) + self.originY

    def draw(self):
        pygame.draw.line(settings.screen, settings.pink, (self.originX, self.originY), (self.nodeX, self.nodeY), 3)
        pygame.draw.circle(settings.screen, self.nodeColor, (self.nodeX, self.nodeY), self.nodeRadius)
        pygame.draw.circle(settings.screen, self.originColor, (self.originX, self.originY), self.originRadius)

    def dimensionChange(self):
        self.originX = settings.windowWidth // 2
        self.originY = settings.windowHeight // 2