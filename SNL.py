import pygame
import tkinter
from random import randint as ri

pygame.init()

width=1366
height=768
win=pygame.display.set_mode((width,height))     #Intialsing window
icon=pygame.image.load("icon.png")
pygame.display.set_caption("Snakes & Ladders")
pygame.display.set_icon(icon)
pygame.display.update()         #We need to update the screen everytime you made a change.

dice_x=["dice_1","dice_2","dice_3","dice_4","dice_5","dice_6"]
dice_1=pygame.image.load("dice1.png")
dice_2=pygame.image.load("dice2.png")
dice_3=pygame.image.load("dice3.png")
dice_4=pygame.image.load("dice4.png")
dice_5=pygame.image.load("dice5.png")
dice_6=pygame.image.load("dice6.png")

red_player=pygame.image.load("redgoti.png")
green_player=pygame.image.load("greengoti.png")

bg=pygame.image.load("playbg.png")
snl=pygame.image.load("Snakes-and-Ladders-Bigger.png")

pixel_wpos=[0,450,500,550,600,650,700,750,800,850,900,0]
pixel_hpos=[600,550,500,450,400,350,300,250,200,150,150]
ladder_pos={1:38,4:14,9:31,21:42,28:84,51:67,72:91,80:99}
snakes_pos={17:6,54:34,62:19,64:60,87:36,93:73,95:75,98:79}

dice_sound=pygame.mixer.Sound("Win.wav")
ladder_sound=pygame.mixer.Sound("ladder.wav")
snake_sound=pygame.mixer.Sound("snake.wav")

#clock=pygame.time.Clock()


red_posw=400                #Initial Positions of players
red_posh=600
green_posw=400
green_posh=600


def dice_pos(dic):
    
    j=30
    win.blit(dice_1,(970,530))
    pygame.display.update()
    pygame.time.delay(j)
    win.blit(dice_2,(970,530))
    pygame.display.update()
    pygame.time.delay(j)
    win.blit(dice_3,(970,530))
    pygame.display.update()
    pygame.time.delay(j)
    win.blit(dice_4,(970,530))
    pygame.display.update()
    pygame.time.delay(j)
    win.blit(dice_5,(970,530))
    pygame.display.update()
    pygame.time.delay(j)
    win.blit(dice_6,(970,530))
    pygame.display.update()
    pygame.time.delay(j)
        
    if(dic==1):
        win.blit(dice_1,(970,530))
    elif(dic==2):
        win.blit(dice_2,(970,530))
    elif(dic==3):
        win.blit(dice_3,(970,530))
    elif(dic==4):
        win.blit(dice_4,(970,530))
    elif(dic==5):
        win.blit(dice_5,(970,530))
    else:
        win.blit(dice_6,(970,530))

    pygame.display.update()

def display():

    #pygame.mixer.Sound.play(sample_sound)
    win.blit(snl,(450,150))    
    win.blit(red_player,(red_posw,red_posh))
    win.blit(green_player,(green_posw,green_posh))
    pygame.display.update()



def player_position(sumx):
    x=sumx//10              #Determines Height
    y=sumx%10               #Determines Width

    global pixel_hpos,pixel_wpos

    
    if(x%2==0):
        posh=pixel_hpos[x]
        posw=pixel_wpos[y]
    else:
        posh=pixel_hpos[x]
        posw=pixel_wpos[11-y]
                        
    if(y==0):               #For Corner Postion
        posh=pixel_hpos[x-1]
        if(x%2==0):
            posw=pixel_wpos[1]
        else:
            posw=pixel_wpos[10]

    return posh,posw


    
def plays():

    sumr=0
    sumg=0
    dice,ladder=0,0
    count=-1
    runn=True
    
    global red_posw,red_posh,green_posh,green_posw
    
    
    while runn:
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
                dice=ri(1,6)
                pygame.mixer.Sound.play(dice_sound)
                count+=1
                print(dice)
                dice_pos(dice)
                
                if(count%2==0):                 #For Red player turn
                    if((sumr+dice)<=100):
                        sumr+=dice
            
                        red_posh,red_posw=player_position(sumr)
                        display()
                        pygame.time.delay(500)
                        
                        if(sumr in ladder_pos):
                            ladder=1
                            pygame.mixer.Sound.play(ladder_sound)
                            sumr=ladder_pos[sumr]
                            red_posh,red_posw=player_position(sumr)
                            display()
                        elif(sumr in snakes_pos):
                            pygame.mixer.Sound.play(snake_sound)
                            sumr=snakes_pos[sumr]
                            red_posh,red_posw=player_position(sumr)
                            display()


                if(count%2!=0):                 #For Green player turn
                    if((sumg+dice)<=100):
                        sumg+=dice
                    
                        green_posh,green_posw=player_position(sumg)
                        display()
                        pygame.time.delay(500)
                        
                        if(sumg in ladder_pos):
                            ladder=1
                            pygame.mixer.Sound.play(ladder_sound)
                            sumg=ladder_pos[sumg]
                            green_posh,green_posw=player_position(sumg)
                            display()
                        elif(sumg in snakes_pos):
                            pygame.mixer.Sound.play(snake_sound)
                            sumg=snakes_pos[sumg]
                            green_posh,green_posw=player_position(sumg)
                            display()

                        
                if(dice==6 or ladder==1):
                    count-=1
                    ladder=0
                    print("count: ",count)
        
        if(sumr==100 or sumg==100):
            run=False
            break
        pygame.display.update()
        
        #clock.tick(60)

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            pygame.quit()
            quit()
            exit(0)
    win.blit(bg,(0,0))
    win.blit(snl,(450,150))
    win.blit(red_player,(400,600))
    win.blit(green_player,(350,600))
    win.blit(dice_1,(970,530))
    pygame.display.update()
    plays()
