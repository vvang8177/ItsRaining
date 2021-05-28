import pygame
from pygame import mixer
import os
import random
import time

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("It's Raining")
CHARATER_IMG = pygame.image.load(os.path.join('images', 'char_remake-bg.png'))
BG_IMG = pygame.image.load(os.path.join('images', 'bg.png'))
PU_IMG = pygame.image.load(os.path.join('images', 'powerup.png'))
PU_RESIZE = pygame.transform.scale(PU_IMG, (100,100))
RAIN_IMG = pygame.image.load(os.path.join('images', 'droplet_rework.png'))
RAIN_IMG_RESIZE = pygame.transform.scale(RAIN_IMG, (20,40))

mixer.init()
RAIN_AUDIO = mixer.Sound('raindrop.wav')
KID_AUDIO = pygame.mixer.Sound('kidslaugh.wav')
THUNDER_AUDIO = mixer.Sound('thunder.wav')
KID_AUDIO.play(-1)
THUNDER_AUDIO.play(-1)
THUNDER_AUDIO.set_volume(0.5)

Turqyoise = (48,213,200)
FPS = 60
DROP_RATE = 5
score = 0
NUMBER_OF_RAINS = 20
RAIN_POSITION = [-50,-25,-75, 0]
multi_rain = []





def spawn_rains(character):
    
    global score

    for i in range (NUMBER_OF_RAINS):

        y_value = random.randint(10,900)
        x_value = random.choice(RAIN_POSITION)
        multi_rain.append(pygame.Rect(y_value,x_value,20,38))

        if multi_rain[i].y == 425:
            multi_rain[i].y = random.choice(RAIN_POSITION)
            multi_rain[i].x = random.randint(10,900)
            RAIN_AUDIO.play()
            score+=3


        if multi_rain[i].colliderect(character):
            multi_rain.remove(multi_rain[i])
            score-=25
    
        #rain_tracker = pygame.draw.rect(WIN, (255,0,0),multi_rain[i], 1)             
        WIN.blit(RAIN_IMG_RESIZE, multi_rain[i])
        multi_rain[i].y+=DROP_RATE
    



def display_score():

    pygame.font.init()
    font = pygame.font.SysFont('calibri', 30)
    display_score = font.render("Score: {0}".format(score), 1, (255,255,255)) 
    WIN.blit(display_score, (10, 10))



def draw_character(character,keys_pressed):    

    WIN.blit(CHARATER_IMG, (character.x, character.y))
    
    if keys_pressed[pygame.K_a] and character.x - 10 > 0:
        character.x -= 10
    if keys_pressed[pygame.K_d] and character.x + 10 < 850:
        character.x += 10
    



# def spawn_powerup(powerup,character):
    
#     power = []
#     power.append(powerup)
#     WIN.blit(PU_RESIZE, powerup)
#     #PU_tracker = pygame.draw.rect(WIN, (0,0,255),powerup, 1)    
#     powerup.y += DROP_RATE

#     if powerup.y >= 355:
#         powerup.y = 355

#     if powerup.colliderect(character):
#         power.remove(powerup)



def main():

    character = pygame.Rect(WIDTH/2,360,53,95)
    powerup = pygame.Rect(random.randint(10,850),-50,100,100)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False


        WIN.blit(BG_IMG,(0,0))
        draw_character(character,keys_pressed = pygame.key.get_pressed())
        spawn_rains(character)
        #spawn_powerup(powerup,character)
        display_score()
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
            