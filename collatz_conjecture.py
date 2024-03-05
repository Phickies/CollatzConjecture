import pygame
import math


class Collatz:

    def __init__(self, number):
        while number != 1:
            number = collatz(number)
            self.collatz_list = []
            self.collatz_list.append(number)

    def visual_display(self, screen, start_position: pygame.Vector2, length, width, direction_angle, rotation_angle):
        # Remove 2 first element for reduce overlap -3
        for i in range(len(self.collatz_list) - 3, -1, -1):
            if self.collatz_list[i] % 2 == 0:
                direction_angle += rotation_angle
            elif self.collatz_list[i] == 1:
                direction_angle -= rotation_angle
            else:
                direction_angle -= rotation_angle * 2

            # Calculating the end position
            next_x = start_position.x + math.cos(math.radians(direction_angle)) * length
            next_y = start_position.y + math.sin(math.radians(direction_angle)) * length

            # Draw a line
            line = pygame.Surface((length, width), pygame.SRCALPHA)

            # Adding color
            red = pygame.Color(255, 20, 20, 10)
            color = red.lerp((255, 255, 20, 10), map_value(start_position.y, screen.get_height(), 0, 0, 1))
            color = color.lerp((0, 200, 0, 1), map_value(start_position.x, screen.get_width(), -screen.get_width() / 2, 0, 1))
            line.fill(color)

            # Rotate it with angle and shift it
            rotated_line = pygame.transform.rotate(line, -direction_angle)

            # draw the rotated line onto the screen
            screen.blit(rotated_line, (start_position.x, start_position.y))

            # Shift the next start position of the line to the head
            start_position.x = next_x
            start_position.y = next_y


def collatz(n: int) -> int:
    if n % 2 == 0:
        return int(n/2)
    else:
        return n*3 + 1


def collatz_step_count(n: int) -> int:
    step_count = 0
    while n != 1:
        n = collatz(n)
        step_count += 1
    return step_count


def map_value(value, from_low, from_high, to_low, to_high):
    """
    Map a value from one range to another.

    :param value: The value to be mapped.
    :param from_low: The minimum value of the original range.
    :param from_high: The maximum value of the original range.
    :param to_low: The minimum value of the target range.
    :param to_high: The maximum value of the target range.
    :return: The mapped value.
    """
    if value < from_high and value < from_low:
        value = from_high
    if value > from_high and value > from_low:
        value = from_high
    if value < from_low and value < from_high:
        value = from_low
    if value > from_low and value > from_high:
        value = from_low
    from_range = from_high - from_low
    to_range = to_high - to_low

    scaled_value = float(value - from_low) / float(from_range)

    return to_low + (scaled_value * to_range)
