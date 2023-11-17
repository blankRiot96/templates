import pygame

pygame.init()
win = pygame.display.set_mode((800, 450))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            raise SystemExit

    win.fill("black")
    pygame.display.update()
