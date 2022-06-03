import pygame
from pygame import mixer

pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Hi Hat')
# use own font and drop it in file structure
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()


def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT], 5)
    bottom_box = pygame.draw.rect(
        screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)


run = True
# as long as run is true, we're going to execute this 60 times per second
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
