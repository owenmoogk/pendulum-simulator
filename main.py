# INIT
import pygame, time, math

pygame.font.init()  # init font
windowWidth = 800
windowHeight = 800
myFont = pygame.font.SysFont("comicsans", 30)
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pendulum Simulation")

# SETTINGS
simSpeed = 30 # ticks / frames per second
gravity = 9.8
mass = 1
dampening = 0.99 # every tick it loses some energy

# COLORS
white = (255,255,255)
grey = (150,150,150)
blue = (51,153,255)
red = (255,0,0)
pink = (254,127,156)
green = (0,255,0)
black = (0,0,0)
backgroundColor = white

# globals
movementConstant = gravity * mass
angle = math.radians(70)
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

    # labels
    score_label = myFont.render("Angle: " + str(round(math.degrees(angle), 4)),1,black)
    screen.blit(score_label, (10, 10))
    score_label = myFont.render("Acceleration: " + str(round(angularAcceleration*100, 4)),1,black)
    screen.blit(score_label, (10, 40))
    score_label = myFont.render("Velocity: " + str(round(angularVelocity*100, 4)),1,black)
    screen.blit(score_label, (10, 70))
    score_label = myFont.render("Mass: " + str(mass),1,black)
    screen.blit(score_label, (10, windowHeight-40))
    score_label = myFont.render("Gravity: " + str(gravity),1,black)
    screen.blit(score_label, (10, windowHeight-70))
    score_label = myFont.render("Dampening: " + str(dampening),1,black)
    screen.blit(score_label, (10, windowHeight-100))

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

    angularAcceleration = -movementConstant * math.sin(angle) / length

    angularVelocity += angularAcceleration
    angularVelocity *= dampening
    angle += angularVelocity
    node.update()
    drawWindow(origin, node)