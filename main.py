import sys
import math
import pygame
from collatz_conjecture import *

# Set up color
black = (0, 0, 0)
white = (255, 255, 255)
cyan = (0, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)

# Setup input
input_list = []
for i in range(1, 100000):
    input_list.append(i)

# Setup length of the segment
length = 1
# Setup width
width = 1
# Setup angle
coefficient = 3

# Setup canvas size
size = (800, 600)

# State
is_running = True

# Setup display
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CollatzConjecture")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # screen.fill(black)

    # Run loop
    if is_running:
        for input_n in input_list:
            print(input_n)
            collatz_list = []
            # Setup initial position
            position = pygame.Vector2(10, 300)
            angle = 0

            while input_n != 1:
                input_n = collatz(input_n)
                collatz_list.append(input_n)

            for i in range(len(collatz_list)-1, -1, -1):
                if collatz_list[i] % 2 == 0:
                    angle += coefficient
                else:
                    angle -= coefficient*2
                next_x = position.x + math.cos(math.radians(angle)) * length
                next_y = position.y + math.sin(math.radians(angle)) * length
                pygame.draw.line(screen, white, position, (next_x, next_y), width)
                position.x = next_x
                position.y = next_y

        is_running = False

        pygame.display.flip()
        pygame.time.Clock().tick(60)
