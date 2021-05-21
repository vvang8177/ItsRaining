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

RAIN_IMG = pygame.image.load(os.path.join('images', 'droplet_rework.png'))
RAIN_IMG_RESIZE = pygame.transform.scale(RAIN_IMG, (20,40))


Turqyoise = (48,213,200)
FPS = 60
DROP_RATE = 5
score = 0
NUMBER_OF_RAINS = 5
multi_rain = []






def spawn_rains(rain, character):
    
    global score
    rain_rect = RAIN_IMG_RESIZE.get_rect()
    #rain_tracker = pygame.draw.rect(WIN, (255,0,0),rain, 1)
    #WIN.blit(RAIN_IMG_RESIZE, (rain.x, rain.y))

    for i in range(NUMBER_OF_RAINS):
        y_value = random.randint(10,900)
        multi_rain.append(pygame.Rect(y_value,50,20,38))

       
    for i in range (NUMBER_OF_RAINS):

        rain_tracker = pygame.draw.rect(WIN, (255,0,0),multi_rain[i], 1)             
        WIN.blit(RAIN_IMG_RESIZE, multi_rain[i])
        multi_rain[i].y+=5


        if rain.y == 425:
            score+=10

        if rain.colliderect(character):
            score-=1
    
    

def display_score():

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    display_score = font.render("Score: {0}".format(score), 1, (255,255,255)) 
    WIN.blit(display_score, (10, 10))



def draw_character(character):    

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




        WIN.fill((Turqyoise))
        keys_pressed = pygame.key.get_pressed()
        draw_character(character)
        spawn_rains(rain, character)
        display_score()
        character_control(keys_pressed, character)
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
            