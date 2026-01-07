import pygame
import settings.settings as set

pygame.init()

# utility functions
def image(sheet, width, height, scale):
    image = pygame.image.load(sheet) 
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image

def image_flip(image, x=False, y=False):
    image = pygame.transform.flip(image, x, y)
    return image

def pos(image, **pos):
    return image.get_rect(**pos) 


screen = pygame.display.set_mode((set.screen_width, set.screen_height))
pygame.display.set_caption("Meow Dodge")

clock = pygame.time.Clock()

# sprites
cat = image('./assets/animals/cat/cat_idle.png', 27, 16, 4)
initial_cat = image_flip(cat, False, False)
flipped_cat = image_flip(cat, True, False)

jump = -20

ground_level = 595
x_velocity = 8
y_velocity = 0
cat_pos = pos(cat, midbottom=(set.screen_width // 2, ground_level))

background = image('./assets/backgrounds/background.png', 1280, 720, 1)
background_pos = pos(background, center=(set.screen_width//2, set.screen_height//2)) 

heart_1 = image('./assets/ui/health/heart.png', 32, 32, 1).convert_alpha()
heart_2 = image('./assets/ui/health/heart.png', 32, 32, 1).convert_alpha()
heart_3 = image('./assets/ui/health/heart.png', 32, 32, 1).convert_alpha()
heart_pos_1 = pos(heart_1, topleft=(set.screen_width - 150, 30))
heart_pos_2 = pos(heart_2, topleft=(set.screen_width - 100, 30))
heart_pos_3 = pos(heart_3, topleft=(set.screen_width - 50, 30))
 
# colors
gray = (50, 50, 50)

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and cat_pos.bottom == ground_level:
                y_velocity = jump 
    key = pygame.key.get_pressed()

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        cat_pos.x -= x_velocity
        cat = flipped_cat
        if cat_pos.left < 0:
            cat_pos.left = 0

    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        cat_pos.x += x_velocity
        cat = initial_cat
        if cat_pos.right > set.screen_width:
            cat_pos.right = set.screen_width

    y_velocity += 1
    cat_pos.y += y_velocity
    if cat_pos.bottom > ground_level:
        cat_pos.bottom = ground_level


    current_time = pygame.time.get_ticks()

    screen.fill(gray)
    screen.blit(background, background_pos)
    screen.blit(heart_1, heart_pos_1)
    screen.blit(heart_2, heart_pos_2)
    screen.blit(heart_3, heart_pos_3)
    screen.blit(cat, cat_pos)

    pygame.display.update()
    clock.tick(set.fps)
pygame.quit()
