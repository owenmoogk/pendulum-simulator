import settings
from math import sin, cos, degrees, radians
import pygame

class Pendulum:
    def __init__(self):

        self.originX = settings.windowWidth // 2
        self.originY = settings.windowHeight // 2
        self.originColor = settings.grey
        self.originRadius = 5

        self.nodeX = settings.length * sin(settings.initAngle) + self.originX
        self.nodeY = settings.length * cos(settings.initAngle) + self.originY
        self.nodeColor = settings.red
        self.nodeRadius = settings.pointRadius

        self.angularAcceleration = 0
        self.angularVelocity = 0
        self.angle = settings.initAngle

    def update(self, deltaTime):

        # cw positive
        print(self.angle)
        tangentialForce = - settings.gravity * settings.mass * sin(self.angle) - self.angularVelocity * settings.dampeningCoefficient
        self.angularAcceleration = tangentialForce / settings.mass
        self.angularVelocity += self.angularAcceleration * deltaTime
        self.angle += self.angularVelocity * deltaTime

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