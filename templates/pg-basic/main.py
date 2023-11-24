import pygame

pygame.init()
win = pygame.display.set_mode((800, 450))
clock = pygame.Clock()


while True:
    dt = clock.tick(60) / 1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            raise SystemExit

    pygame.display.set_caption(f"{clock.get_fps():.0f}")

    win.fill("black")
    pygame.display.update()
