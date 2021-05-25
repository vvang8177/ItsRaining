import pygame
from pygame import mixer
import os
import random
import time

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("It's Raining")
CHARATER_IMG = pygame.image.load(os.path.join('images', 'char.png'))
#CHARATER_IMG_RESIZE = pygame.transform.scale(CHARATER_IMG, (100,100))
#CHARATER_IMG_ROTATE = pygame.transform.rotate(pygame.transform.scale(CHARATER_IMG, (100,100)), 180)
BG_IMG = pygame.image.load(os.path.join('images', 'bg.png'))

RAIN_IMG = pygame.image.load(os.path.join('images', 'droplet_rework.png'))
RAIN_IMG_RESIZE = pygame.transform.scale(RAIN_IMG, (20,40))

mixer.init()
RAIN_AUDIO = mixer.Sound('raindrop.wav')
KID_AUDIO = pygame.mixer.Sound('kidslaugh.wav')
THUNDER_AUDIO = mixer.Sound('thunder.wav')
KID_AUDIO.play(-1)
THUNDER_AUDIO.play(-1)
THUNDER_AUDIO.set_volume(0.6)

Turqyoise = (48,213,200)
FPS = 60
DROP_RATE = 5
score = 0
NUMBER_OF_RAINS = 10
RAIN_POSITION = [-50,-25,-75, 0]
multi_rain = []




def spawn_rains(rain, character):
    
    global score
    rain_rect = RAIN_IMG_RESIZE.get_rect()
    #rain_tracker = pygame.draw.rect(WIN, (255,0,0),rain, 1)
    #WIN.blit(RAIN_IMG_RESIZE, (rain.x, rain.y))

       
    for i in range (NUMBER_OF_RAINS):

        y_value = random.randint(10,900)
        x_value = random.choice(RAIN_POSITION)
        multi_rain.append(pygame.Rect(y_value,x_value,20,38))

        if multi_rain[i].y == 425:
            multi_rain[i].y = random.choice(RAIN_POSITION)
            multi_rain[i].x = random.randint(10,900)
            RAIN_AUDIO.play()
            score+=5


        if multi_rain[i].colliderect(character):
            score-=3
    
        #rain_tracker = pygame.draw.rect(WIN, (255,0,0),multi_rain[i], 1)             
        WIN.blit(RAIN_IMG_RESIZE, multi_rain[i])
        multi_rain[i].y+=5
    



def display_score():

    pygame.font.init()
    font = pygame.font.SysFont('calibri', 30)
    display_score = font.render("Score: {0}".format(score), 1, (255,255,255)) 
    WIN.blit(display_score, (10, 10))



def draw_character(character):    

    WIN.blit(BG_IMG, (0,0))
    WIN.blit(CHARATER_IMG, (character.x, character.y))
    char_rect = CHARATER_IMG.get_rect()
    #char_tracker = pygame.draw.rect(WIN, (255,0,0),character, 1)    

    

def character_control(keys_pressed, character):

    if keys_pressed[pygame.K_a] and character.x - 10 > 0:
        character.x -= 10
    if keys_pressed[pygame.K_d] and character.x + 10 < 800:
        character.x += 10



def main():

    character = pygame.Rect(WIDTH/2,350,100,110)
    rain = pygame.Rect(random.randint(10,800),-50,20,38)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False



        keys_pressed = pygame.key.get_pressed()
        draw_character(character)
        spawn_rains(rain, character)
        display_score()
        character_control(keys_pressed, character)
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
            