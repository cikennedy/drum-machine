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
beats = 8
instruments = 6


def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(
        screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Kick', True, white)
    screen.blit(kick_text, (30, 230))
    crash_cymbal_text = label_font.render('Crash', True, white)
    screen.blit(crash_cymbal_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    tom_text = label_font.render('Tom', True, white)
    screen.blit(tom_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(
            screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)

    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(
                screen, gray, [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200) // instruments)], 5, 5)
            # returning the rectangle of each beat, also returning the x and y coordinate of it
            boxes.append((rect, (i, j)))
    return boxes


run = True
# as long as run is true, we're going to execute this 60 times per second
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # everytime we update the total beats, that list is going to change so it has to be the length of boxes
            for i in range(len(boxes)):
                # position at which the mouse button was when the mousedown occurs
                if boxes[i][0].colliderect(event.pos):
                    coords = boxes[i][1]

    pygame.display.flip()
pygame.quit()
