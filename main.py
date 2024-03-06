from collatz_conjecture import *
import sys

# Setup input
input_list = []
for i in range(1, 50000):
    input_list.append(i)


# Setup canvas size
size = (800, 800)

# State
is_running = True

# Setup display
pygame.init()
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("CollatzConjecture")

while True:
    # Run loop
    if is_running:
        for input_n in input_list:

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            # Setup initial position
            position = pygame.Vector2(size[0]/2, size[1]-1)

            if not input_n % 2 == 0:
                clz = Collatz(input_n)
                clz.visual_display(screen, position, 5, 2, 270, 6.5)

            pygame.display.flip()

        is_running = False
    pygame.time.Clock().tick(60)
