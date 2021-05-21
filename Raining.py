import pygame
import os
import random
import time


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("It's Raining")
CHARATER_IMG = pygame.image.load(os.path.join('images', 'char.png'))
#CHARATER_IMG_RESIZE = pygame.transform.scale(CHARATER_IMG, (100,100))
#CHARATER_IMG_ROTATE = pygame.transform.rotate(pygame.transform.scale(CHARATER_IMG, (100,100)), 180)

RAIN_IMG = pygame.image.load(os.path.join('images', 'droplet.png'))
RAIN_IMG_RESIZE = pygame.transform.scale(RAIN_IMG, (40,40))


Turqyoise = (48,213,200)
FPS = 60
DROP_RATE = 5
score = 0

def draw_window(character, rain):    
    global score

    WIN.fill((Turqyoise))
    WIN.blit(CHARATER_IMG, (character.x, character.y))
    WIN.blit(RAIN_IMG_RESIZE, (rain.x, rain.y))
    
    char_rect = CHARATER_IMG.get_rect()
    rain_rect = RAIN_IMG_RESIZE.get_rect()

    rain.y += DROP_RATE
    score+=1

    if rain.y == 425:
        rain.x = random.randrange(10, 800)
        rain.y = 0


    if rain.colliderect(character):
        score-=6


    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    display_score = font.render("Score: {0}".format(score), 1, (255,255,255)) 
    WIN.blit(display_score, (10, 10))

    pygame.display.update()
    

def character_control(keys_pressed, character):
    if keys_pressed[pygame.K_a] and character.x - 10 > 0:
        character.x -= 10
    if keys_pressed[pygame.K_d] and character.x + 10 < 800:
        character.x += 10


def main():
    character = pygame.Rect(WIDTH/2,350,100,100)
    rain = pygame.Rect(50,50,40,40)


    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()
        character_control(keys_pressed, character)
        draw_window(character, rain)


    pygame.quit()

if __name__ == "__main__":
    main()
            