import pygame


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self) -> pygame.Vector2:
        return pygame.Vector2(self.x, self.y)
