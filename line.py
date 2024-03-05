import math
import pygame
from point import Point


class Line:

    width = 1

    def __init__(self, head_point: Point | pygame.Vector2 | tuple, tail_point: Point | pygame.Vector2 | tuple, color):
        if isinstance(head_point, tuple):
            self.head_x = head_point[0]
            self.head_y = head_point[1]
        else:
            self.head_x = head_point.x
            self.head_y = head_point.y
        if isinstance(tail_point, tuple):
            self.tail_x = tail_point[0]
            self.tail_y = tail_point[1]
        else:
            self.tail_x = tail_point.x
            self.tail_y = tail_point.y
        self.length = math.sqrt(pow(self.tail_x-self.head_x, 2)+pow(self.tail_y-self.head_y, 2))
        self.color = color

    def head(self) -> pygame.Vector2:
        return pygame.Vector2(self.head_x, self.head_y)

    def tail(self) -> pygame.Vector2:
        return pygame.Vector2(self.tail_x, self.tail_y)

    def draw(self, screen, color, start_point: Point | pygame.Vector2, length: pygame.Vector2):
        pygame.draw.line(screen, color, start_point, start_point+length, 1)
