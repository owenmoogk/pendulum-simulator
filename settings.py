from math import radians
import pygame
from pygame.locals import *

# SETTINGS
windowWidth = 800
windowHeight = 800
screen = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)
pygame.display.set_caption("Pendulum Simulation")
pygame.font.init()  # init font
myFont = pygame.font.SysFont("comicsans", 30)

simSpeed = 30 # ticks / frames per second
gravity = 9.8
mass = 1
dampening = 0.995 # every tick it loses some energy
length = 300
initAngle = radians(539)
movementConstant = gravity * mass

# COLORS
white = (255,255,255)
grey = (150,150,150)
blue = (51,153,255)
red = (255,0,0)
pink = (254,127,156)
green = (0,255,0)
black = (0,0,0)
backgroundColor = white

# graphing potential energy constant
potentialConst = 0.0033