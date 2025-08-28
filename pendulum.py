import settings
from math import sin, cos, degrees, radians
import pygame

nodeColor = settings.red
nodeRadius = settings.pointRadius

class Pendulum:
    def __init__(self):

        self.originX = settings.windowWidth // 2
        self.originY = settings.windowHeight // 2
        self.originColor = settings.grey
        self.originRadius = 5

        self.angularAcceleration = 0
        self.angularVelocity = 0
        self.angle = settings.initAngle

    def update(self, deltaTime):

        # cw positive
        print(self.angle)
        tangentialForce = - settings.gravity * settings.mass * sin(self.angle)
        self.angularAcceleration = tangentialForce / settings.mass
        self.angularVelocity += self.angularAcceleration * deltaTime
        self.angularVelocity *= settings.dampeningCoefficient
        self.angle += self.angularVelocity * deltaTime

        if degrees(self.angle) > 180:
            self.angle -= radians(360)
        if degrees(self.angle) < -180:
            self.angle += radians(360)

    def getCoords(self):
        nodeX = settings.length * sin(self.angle) + self.originX
        nodeY = settings.length * cos(self.angle) + self.originY
        return [nodeX, nodeY]
    
    def getMassVelocity(self):
        return self.angularVelocity * settings.length * settings.pixelToMeter

    def draw(self):
        [nodeX, nodeY] = self.getCoords()
        pygame.draw.line(settings.screen, settings.pink, (self.originX, self.originY), (nodeX, nodeY), 3)
        pygame.draw.circle(settings.screen, nodeColor, (nodeX, nodeY), nodeRadius)
        pygame.draw.circle(settings.screen, self.originColor, (self.originX, self.originY), self.originRadius)

    def dimensionChange(self):
        self.originX = settings.windowWidth // 2
        self.originY = settings.windowHeight // 2