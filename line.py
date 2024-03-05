import pygame


class Line:

    def __init__(self, head_x, head_y, tail_x, tail_y, color):
        self.head_x = head_x
        self.head_y = head_y
        self.tail_x = tail_x
        self.tail_y = tail_y
        self.color = color
        self._placeholder = pygame.Surface((abs(tail_x-head_x), abs(tail_y-head_y)))

    def head_position(self) -> pygame.Vector2:
        return pygame.Vector2(self.head_x, self.head_y)

    def tail_position(self) -> pygame.Vector2:
        return pygame.Vector2(self.tail_x, self.tail_y)

    def display(self, screen):
        pygame.draw.line(screen, self.color, self.head_position(), self.tail_position())
        screen.blit(self._placeholder, self.head_x, self.head_y)
