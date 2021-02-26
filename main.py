# INIT
import pygame, time, math

pygame.font.init()  # init font
windowWidth = 800
windowHeight = 800
myFont = pygame.font.SysFont("comicsans", 50)
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pendulum Simulation")

# SETTINGS
simSpeed = 30 # ticks / frames per second
gravity = 9.8
dampening = 0.99 # every tick it loses some energy

# COLORS
white = (255,255,255)
grey = (150,150,150)
blue = (51,153,255)
red = (255,0,0)
pink = (254,127,156)
green = (0,255,0)
backgroundColor = white

# globals
angle = math.pi / 4
angularVelocity = 0
angularAcceleration  = 0
length = 400

class Origin:
    def __init__(self):
        self.x = windowWidth / 2
        self.y = 100
        self.color = grey
        self.radius = 10

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def getForce(self, node):
        acceleration = gravity * self.angle
        direction = self.angle

        node.xVel = acceleration * math.sin(direction)
        node.yVel = acceleration * math.cos(direction)

class Node:
    def __init__(self):
        self.x = length * math.sin(angle) + origin.x
        self.y = length * math.cos(angle) + origin.y
        self.xVel = 0
        self.yVel = 0
        self.color = red
        self.radius = 40

    def update(self):
        self.y = length * math.cos(angle) + origin.y
        self.x = length * math.sin(angle) + origin.x

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def drawWindow(origin, node):
    screen.fill(backgroundColor)
    pygame.draw.line(screen, pink, (node.x, node.y), (origin.x, origin.y), 3)
    origin.draw()
    node.draw()
    pygame.display.update()

clock = pygame.time.Clock()

origin = Origin()
node = Node()

while True:
    clock.tick(simSpeed)

    # quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    angularAcceleration = -0.01 * math.sin(angle)

    angularVelocity += angularAcceleration
    angularVelocity *= dampening
    angle += angularVelocity
    node.update()
    drawWindow(origin, node)