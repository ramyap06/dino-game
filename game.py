import pygame
from sys import exit
import random

WIDTH = 800
HEIGHT = 400

def random_choice():
    choices = [med_cactus, small_cactus, big_cactus, two_cactus, bird]
    selected = random.choice(choices)
    rect = med_cactus_rect
    if selected == small_cactus:
        rect = small_cactus_rect
    elif selected == big_cactus:
        rect = big_cactus_rect
    elif selected == two_cactus:
        rect = two_cactus_rect
    elif selected == bird:
        rect = bird_rect
    return selected, rect

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My First Game!')
clock = pygame.time.Clock()

curr_font = pygame.font.Font(r'C:\Users\ramya\OneDrive\Documents\GitHub\dino-game\Pixeltype.ttf', 30)

sky = pygame.Surface((WIDTH, 300))
sky.fill('white')
ground = pygame.Surface((WIDTH, 100))
ground.fill('white')

curr_score = 0
high_score = 0

text = curr_font.render(f'HI  {high_score:05}  {curr_score:05}', True, 'Black')

dino = pygame.image.load(r'C:\Users\ramya\OneDrive\Documents\GitHub\dino-game\dino.png').convert_alpha()
dino = pygame.transform.scale(dino, (50, 55))
dino_rect = dino.get_rect(bottomleft = (5, 300))

med_cactus = pygame.image.load(r'C:\Users\ramya\OneDrive\Documents\GitHub\dino-game\cactus.png').convert_alpha()
med_cactus = pygame.transform.scale(med_cactus, (30, 60))
med_cactus_rect = med_cactus.get_rect(bottomright = (0, 312))

small_cactus = pygame.image.load(r'C:\Users\ramya\OneDrive\Documents\GitHub\dino-game\small_cactus.png').convert_alpha()
small_cactus = pygame.transform.scale(small_cactus, (25, 45))
small_cactus_rect = small_cactus.get_rect(bottomright = (0, 310))

big_cactus = pygame.image.load(r'C:\Users\ramya\OneDrive\Documents\GitHub\dino-game\big_cactus.png').convert_alpha()
big_cactus = pygame.transform.scale(big_cactus, (80, 60))
big_cactus_rect = big_cactus.get_rect(bottomright = (0, 308))

two_cactus = pygame.image.load(r'C:\Users\ramya\OneDrive\Documents\GitHub\dino-game\two_cactus.png').convert_alpha()
two_cactus = pygame.transform.scale(two_cactus, (50, 60))
two_cactus_rect = two_cactus.get_rect(bottomright = (0, 312))

bird = pygame.image.load(r'C:\Users\ramya\OneDrive\Documents\GitHub\dino-game\bird.png').convert_alpha()
bird = pygame.transform.scale(bird, (40, 35))
bird_rect = bird.get_rect(bottomright = (0, 280))

choice = med_cactus
rect = med_cactus_rect
gravity = 0
game_active = True

while True:
    # be able to close the window
    # look for all possible events, things done to computer like signals
    for event in pygame.event.get():
        # if QUIT, universal code for x button, then quit
        if event.type == pygame.QUIT:
            pygame.quit()
            # exits the program via os kernel-system call
            exit()
    
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                #print("JUMP!")
                #dino_rect.y -= 110
    
    screen.blit(sky, (0,0))
    screen.blit(ground, (0, 300))
    screen.blit(text, (640, 10))
    curr_score += 1
    text = curr_font.render(f'HI  {high_score:05}  {curr_score:05}', True, 'Black')
    pygame.draw.line(screen, (92, 92, 91), (0, 300), (800, 300), 2)

    gravity += 1
    dino_rect.y += gravity
    if dino_rect.bottom >= 300:
        dino_rect.bottom = 300
    screen.blit(dino, dino_rect)

    if game_active:
        if rect.right <= 0:
            choice, rect = random_choice()
            rect.left = 800
        rect.x -= 5
        screen.blit(choice, rect)
        
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and dino_rect.bottom >= 300:
            gravity = -17
        
        if rect.colliderect(dino_rect):
            game_active = False
        
    else:
        screen.blit(choice, rect)
        text = curr_font.render('GAME OVER', True, 'Black')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            choice, rect = random_choice()
            rect.left = 800
            if high_score < curr_score:
                high_score = curr_score
            curr_score = 0
            game_active = True

    # keep updating the display & make sure it stays
    pygame.display.update()
    clock.tick(60)