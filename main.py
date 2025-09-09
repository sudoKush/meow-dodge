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

def pos(image, pos_x, pos_y):
    pos = image.get_rect(center=(pos_x, pos_y))
    return pos


screen = pygame.display.set_mode((set.screen_width, set.screen_height))
pygame.display.set_caption("Meow Dodge")

clock = pygame.time.Clock()

# sprites
cat = image('./assets/animals/cat/cat_idle.png', 27, 16, 8)
initial_cat = image_flip(cat, False, False)
flipped_cat = image_flip(cat, True, False)

velocity = 8
cat_pos = pos(cat, set.screen_width // 2, set.screen_height // 2) 

# colors
gray = (50, 50, 50)

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    keys = pygame.key.get_pressed()
    w_key = keys[pygame.K_w]
    a_key = keys[pygame.K_a]
    s_key = keys[pygame.K_s]
    d_key = keys[pygame.K_d]

    if w_key:
        cat_pos.y -= velocity
        if cat_pos.y < 0: # prevent going above the screen
            cat_pos.y = 0

    if a_key:
        cat = flipped_cat
        cat_pos.x -= velocity
        if cat_pos.x < 0: # prevent going off left 
            cat_pos.x = 0

    if s_key:
        cat_pos.y += velocity
        if cat_pos.bottom > set.screen_height: # prevent going off bottom
            cat_pos.bottom = set.screen_height

    if d_key:
        cat = initial_cat
        cat_pos.x += velocity
        if cat_pos.right > set.screen_width: # prevent going off right 
            cat_pos.right = set.screen_width

    if w_key and a_key or w_key and d_key or s_key and a_key or s_key and d_key:
        velocity = 6
    else: 
        velocity = 8

    screen.fill(gray)
    screen.blit(cat, cat_pos)

    pygame.display.update()
    clock.tick(set.fps)
pygame.quit()
