import pygame
import random

pygame.init()

screen=pygame.display.set_mode((890, 550))
pygame.display.set_caption("Duck Hunt")

black = (0, 0, 0)
white=(225,225,225)
red=(225,0,0)


def game():
    run=True
    x_pos = 0
    y_pos = 0

    x_click = 0
    y_click = 0

    x_duck = 0
    y_duck = random.randint(0, 450)
    
    points = 0
    velocity = 2
    errorState = False
    
    button_l=200
    button_b=50
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif event.type == pygame.MOUSEMOTION:
                x_pos, y_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_click, y_click = pygame.mouse.get_pos()
                pygame.mixer.music.load("shot.mp3")
                pygame.mixer.music.play()

        position = (x_pos - 50, y_pos - 50)

        x_duck += 1

        if x_duck * velocity > 890 and not errorState:
            x_duck = 0
            y_duck = random.randint(0, 450)
            errorState = True

        screen.fill(black)
        pygame.mouse.set_visible(False)
        
        screen.blit(pygame.image.load("background.png"), (0, 0))
        screen.blit(pygame.font.SysFont("tahoma", 36).render("Score: " + str(points), True, white), (700, 450))

        if x_click in range(x_duck * velocity - 30, x_duck * velocity + 30) and y_click in range(y_duck - 30, y_duck + 30):
            points += 1
            velocity += 1
            x_duck = 0
            y_duck = random.randint(50, 500)
            
        screen.blit(pygame.image.load("duck.gif"), (x_duck * velocity, y_duck))

        if errorState:
            x_duck = -50
            y_duck = -50
            screen.blit(pygame.font.SysFont("tahoma", 36).render("GAME OVER",True,red),(350,200))
            pygame.draw.rect(screen,red,(350,300,button_l+20,button_b))
            pygame.draw.rect(screen,red,(400,400,button_l-100,button_b))
            screen.blit(pygame.font.SysFont("tahoma", 36).render("PLAY AGAIN",True,black),(360,300))
            screen.blit(pygame.font.SysFont("tahoma", 36).render("QUIT",True,black),(410,400))

        screen.blit(pygame.image.load("gun.gif").convert(), position)
        pygame.display.update()
        
        if x_click in range(350, 350+button_l) and y_click in range(300,300+button_b):
            game()
        if x_click in range(400, 400+button_l) and y_click in range(400,400+button_b):
            run=False
            
        
    pygame.quit()

def intro():
    intro=True
    x_click=0
    y_click=0
    button_l=100
    button_b=50

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                intro=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_click, y_click = pygame.mouse.get_pos()
            screen.fill(black)
            screen.blit(pygame.image.load("background.png"), (0, 0))
            
            pygame.draw.rect(screen,red,(370,200,button_l,button_b))
            pygame.draw.rect(screen,red,(370,300,button_l,button_b))
            screen.blit(pygame.font.SysFont("tahoma", 36).render("PLAY",True,black),(380,200))
            screen.blit(pygame.font.SysFont("tahoma", 36).render("QUIT",True,black),(380,300))
            pygame.display.update()
            if x_click in range(370, 370+button_l) and y_click in range(200,200+button_b):
                game()
            if x_click in range(370, 370+button_l) and y_click in range(300,300+button_b):
                intro=False
    pygame.quit()
            
            
intro()
     

