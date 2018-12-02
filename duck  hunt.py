import pygame
import random

pygame.init()

#screen specifications
screen=pygame.display.set_mode((890, 550))
pygame.display.set_caption("Duck Hunt")

black = (0, 0, 0)
white=(225,225,225)
red=(225,0,0)

#duck hunt game code
def game():
    run=True
    #variables for position of the mouse & duck
    x_pos = 0
    y_pos = 0

    x_click = 0
    y_click = 0

    x_duck = 0
    y_duck = random.randint(0, 450)
    
    points = 0
    velocity = 2
    errorState = False
    
    #in game button length & breadth
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

        #condition if duck passes the screen ( if the duck is not shot)---- part1
        if x_duck * velocity > 890 and not errorState:
            x_duck = 0
            y_duck = random.randint(0, 450)
            errorState = True
         
        #screen specification while the background is not loaded(screen not updated) 
        screen.fill(black)
        pygame.mouse.set_visible(False)
        
        #screen background and points tally 
        screen.blit(pygame.image.load("background.png"), (0, 0))
        screen.blit(pygame.font.SysFont("tahoma", 36).render("Score: " + str(points), True, white), (700, 450))

        #condition if the duck is shot
        if x_click in range(x_duck * velocity - 30, x_duck * velocity + 30) and y_click in range(y_duck - 30, y_duck + 30):
            points += 1
            velocity += 1
            x_duck = 0
            y_duck = random.randint(50, 500)
            
        #image of the duck
        screen.blit(pygame.image.load("duck.gif"), (x_duck * velocity, y_duck))

        #condition if duck is not shot-----part2
        if errorState:
            x_duck = -50
            y_duck = -50
            #game over appearance code
            screen.blit(pygame.font.SysFont("tahoma", 36).render("GAME OVER",True,red),(350,200))
            #play again & quit buttons
            pygame.draw.rect(screen,red,(350,300,button_l+20,button_b))
            pygame.draw.rect(screen,red,(400,400,button_l-100,button_b))
            screen.blit(pygame.font.SysFont("tahoma", 36).render("PLAY AGAIN",True,black),(360,300))
            screen.blit(pygame.font.SysFont("tahoma", 36).render("QUIT",True,black),(410,400))

        #mouse pointer image
        screen.blit(pygame.image.load("gun.gif").convert(), position)
        #screen update 
        pygame.display.update()
        
        #condition if user clicks on play again button after game is over
        if x_click in range(350, 350+button_l) and y_click in range(300,300+button_b):
            game()
        #condition if user clicks on quit button after game is over
        if x_click in range(400, 400+button_l) and y_click in range(400,400+button_b):
            run=False

#intro screen code
def intro():
    intro=True
    #mouse variables
    x_click=0
    y_click=0
    #button variables
    button_l=100
    button_b=50

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                intro=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_click, y_click = pygame.mouse.get_pos()
            
            #screen specification while the background is not loaded(screen not updated) 
            screen.fill(black)
            screen.blit(pygame.image.load("background.png"), (0, 0))
            #play &quit buttons
            pygame.draw.rect(screen,red,(370,200,button_l,button_b))
            pygame.draw.rect(screen,red,(370,300,button_l,button_b))
            screen.blit(pygame.font.SysFont("tahoma", 36).render("PLAY",True,black),(380,200))
            screen.blit(pygame.font.SysFont("tahoma", 36).render("QUIT",True,black),(380,300))
            #screen update
            pygame.display.update()
            #condition if user clicks on play
            if x_click in range(370, 370+button_l) and y_click in range(200,200+button_b):
                game()
                intro=False
            #condition if user clicks on quit
            if x_click in range(370, 370+button_l) and y_click in range(300,300+button_b):
                intro=False
    #close window command
    pygame.quit()
            
#main          
intro()
     

