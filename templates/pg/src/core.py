import asyncio

import pygame

from . import shared


class Core:
    def __init__(self) -> None:
        self.win_init()

        shared.dt = 0.0
        shared.events = []

    def win_init(self) -> None:
        pygame.init()
        shared.screen = pygame.display.set_mode(shared.WIN_SIZE)
        shared.clock = pygame.time.Clock()
        pygame.display.set_caption("Title")

    def update(self) -> None:
        shared.events = pygame.event.get()
        for event in shared.events:
            if event.type == pygame.QUIT:
                raise SystemExit

        shared.dt = shared.clock.tick() / 1000
        shared.dt = min(shared.dt, 0.1)

        shared.keys = pygame.key.get_pressed()
        shared.mouse_pos = pygame.mouse.get_pos()

    def draw(self) -> None:
        shared.screen.fill("black")
        pygame.display.flip()

    async def run(self) -> None:
        while True:
            self.update()
            self.draw()
            await asyncio.sleep(0)
