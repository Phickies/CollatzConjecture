import pygame
import math
from pygame.locals import *
SIZE = 800, 800
pygame.init()
screen = pygame.display.set_mode(SIZE)
FPSCLOCK = pygame.time.Clock()
done = False
screen.fill((0, 0, 0))
degree=0
radar = (100,100)
radar_len = 100
angle = 0

while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
    # then render the line radar->(x,y)
    screen.fill(Color("black"))
    x = radar[0] + math.cos(math.radians(angle)) * radar_len
    y = radar[1] + math.sin(math.radians(angle)) * radar_len
    pygame.draw.line(screen, Color("white"), radar, (x, y), 1)
    pygame.display.flip()
    angle += -1
    FPSCLOCK.tick(40)