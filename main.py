import pygame
import settings.settings as set

pygame.init()

screen = pygame.display.set_mode((set.screen_width, set.screen_height))
pygame.display.set_caption("Meow Dodge")

clock = pygame.time.Clock()

playing = True

# Colors
gray = (50, 50, 50)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    screen.fill(gray)

    pygame.display.update()
    clock.tick(set.fps)
pygame.quit()



