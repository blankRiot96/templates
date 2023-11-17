import pygame

# Constants
WIN_WIDTH = 1200.0
WIN_HEIGHT = 650.0
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)


# Shared variables
screen: pygame.Surface
clock: pygame.Clock
events: list[pygame.event.Event]
keys: list[bool]
dt: float
mouse_pos: pygame.Vector2
