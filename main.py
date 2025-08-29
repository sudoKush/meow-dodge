import pygame, sys
import settings.settings as set

pygame.init()

screen = pygame.display.set_mode((set.SCREEN_WIDTH, set.SCREEN_HEIGHT))
pygame.display.set_caption("Meow Dash")

clock = pygame.time.Clock()

cat_image = pygame.image.load('./assets/animals/cat/protagonist_cat/cat_idle/cat_idle.xcf')
cat_image = pygame.transform.scale(cat_image, (300, 300))

xflipped_cat = pygame.transform.flip(cat_image, True, False)
yflipped_cat = pygame.transform.flip(cat_image, False, True)

cat = cat_image 

cat_rect = cat.get_rect()

speed = 7 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cat_rect.y -= speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cat = xflipped_cat
        cat_rect.x -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cat_rect.y += speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cat = cat_image
        cat_rect.x += speed

    # bg
    screen.fill((150, 150, 150))

    screen.blit(cat, cat_rect)

    pygame.display.update()
    clock.tick(set.FPS)

