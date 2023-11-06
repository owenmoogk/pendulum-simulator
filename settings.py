from math import radians
import pygame
from pygame.locals import *

# DISPLAY
windowWidth = 800
windowHeight = 800
screen = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)
pygame.display.set_caption("Pendulum Simulation")
pygame.font.init()  # init font
myFont = pygame.font.SysFont("comicsans", 30)
pointRadius = 20

# PHYSICS
simSpeed = 30 # ticks / frames per second
gravity = 9.8 # meters per second
mass = 1
dampeningCoefficient = 0.1 # how much the dampening forces increases with velocity (N/(m/s))
length = 300
pixelToMeter = 1/300.0
initAngle = radians(539)

# COLORS
white = (255,255,255)
grey = (150,150,150)
blue = (51,153,255)
red = (255,0,0)
pink = (254,127,156)
green = (0,255,0)
black = (0,0,0)
backgroundColor = white