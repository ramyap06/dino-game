import pygame
from sys import exit

WIDTH = 800
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My First Game!')

curr_font = pygame.font.Font(r'dino-game\Pixeltype.ttf', 30)

sky = pygame.image.load(r'dino-game\sky.png')
print(f"{sky.get_width()}, {sky.get_height()}")
ground = pygame.image.load(r'dino-game\ground.png')

curr_score = 0
high_score = 0
text = curr_font.render(f'HI  {curr_score:05}  {high_score:05}', False, 'Black')

dino = pygame.image.load(r'dino-game\dino-removebg-preview.png')
dino = pygame.transform.scale(dino, (60, 60))
dino_pos = 250

#sample_surface = pygame.Surface((100,100))
#sample_surface.fill('pink')

while True:
    # be able to close the window
    # look for all possible events, things done to computer like signals
    for event in pygame.event.get():
        # if QUIT, universal code for x button, then quit
        if event.type == pygame.QUIT:
            pygame.quit()
            # exits the program via os kernel-system call
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                print("JUMP!")
                dino_pos -= 100
    
    screen.blit(sky, (0,0))
    screen.blit(ground, (0, 300))
    screen.blit(text, (640, 10))

    if dino_pos != 250:
        dino_pos += 0.5
    screen.blit(dino, (0, dino_pos))
    #screen.blit(sample_surface, (150,50))

    # keep updating the display & make sure it stays
    pygame.display.update()
