
# cartesian sign systam in pygame

# pygame me +x vector me +ve hai eg +x axis +10
# pygame me -x vector me -ve hai eg -x axis -10
# pygame me +y vector me -ve hai eg +y axis -10
# pygame me -y vector me +ve hai eg -y axis +10





# import pygame




# # Creating window

# x=pygame.init()
# print(x)
# gameWindow = pygame.display.set_mode((1200,500))
# pygame.display.set_caption("My first Game")




# #Game specific variable

# exit_game=False

# game_over=False


# #creating a game loop
# while not exit_game:
#     for event in pygame.event.get():
#         if event.type==pygame.quit:
#             exit_game=True

#         if event.type==pygame.KEYDOWN:
#             if event.key== pygame.K_RIGHT:
#                 print("you have pressed right arrow key")

        
# pygame.quit()
# quit()







# Snake Game


import pygame
pygame.init()


import os
import random

# # Creating window

screen_width=900
screen_height=600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#backgroung image
welcbgimg=pygame.image.load("welcome_background.jpg")
welcbgimg=pygame.transform.scale(welcbgimg,(screen_width,screen_height)).convert_alpha()
bgimg=pygame.image.load("game_background.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
gobgimg=pygame.image.load("gameover_background.jpg")
gobgimg=pygame.transform.scale(gobgimg,(screen_width,screen_height)).convert_alpha()


#GAME TITLE

pygame.display.set_caption("snakes")
pygame.display.update()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,60)






#colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)









def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_size(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color, [x,y,snake_size, snake_size])




#welcome screen

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(welcbgimg,(0,0))
        
        # text_screen("Welcome to snakes", black, 240,230)
        # text_screen("Press Enter to Play", black, 242,270)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(60)








# #creating a game loop


def gameloop():

    # #Game specific variable

    exit_game=False
    game_over=False
    snake_x=45
    snake_y=45
    velocity_x=0
    velocity_y=0
    snake_size=20
    food_size=20
    food_x=random.randint(0,screen_width/1.25)
    food_y=random.randint(0,screen_height/1.25)
    score=0
    init_velocity=5
    fps=60

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

        
    with open("highscore.txt","r")as f:
        highscore=f.read()

    snk_list=[]
    snk_length=1


    while not exit_game:

        if game_over:
            with open("highscore.txt","w")as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(gobgimg,(0,0))

            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    exit_game=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_DOWN:
                        velocity_x=0
                        velocity_y=init_velocity
                    if event.key==pygame.K_UP:
                        velocity_x=0
                        velocity_y=-init_velocity

                    
                    #cheat  code
                    if event.key==pygame.K_q:
                        score+=10
                    






            snake_x= snake_x+velocity_x
            snake_y= snake_y+velocity_y

            if abs(snake_x - food_x)<= 15 and abs(snake_y - food_y)<=15:
                score += 10
                if score>int(highscore):
                    highscore=score
                food_x=random.randint(0,screen_width/1.25)
                food_y=random.randint(0,screen_height/1.25)
                snk_length += 5



            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))

            text_screen("Score: "+str(score)+ " High Score: "+highscore, white, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                

            plot_size(gameWindow, black, snk_list, snake_size)

        clock.tick(fps)
        pygame.display.update()



    pygame.quit()
    quit()


welcome()




