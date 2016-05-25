import pygame
import random
#import os
pygame.init()

red =(255,0,0)
white=(255,255,255)
black=(0,0,0)
gray=(128,128,128)
blue=(0,150,200)
green= (0,255,0)

clock = pygame.time.Clock()

gameDisplay=pygame.display.set_mode((500,650))
pygame.display.set_caption("Atrasados do Insper")
    

img = pygame.image.load("personagem.png")
img2 = pygame.image.load("Rua_2.png")
img3 = pygame.image.load("carrov.png")
img4 = pygame.image.load("carroa.png")
imgr = pygame.image.load("ashes2.png")
imgl = pygame.image.load("ashes3.png")


pygame.display.update()


gameExit= False


persoX= 100
persoY= 650

lead_x=300
lead_y=550 


#PAREDE 1
j= random.randint(0,2)
lista = [100,200,300]
ParedeX= lista [j]
ParedeY= 0
lead_y_change= 0





littlefont = pygame.font.SysFont("comicsansms", 20)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)
large1font = pygame.font.SysFont("hightowertext", 50)




def pause():
    
    paused = True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Pause",
                          red, -100, size = "large")
        message_to_screen("Pressione C para continuar ou Q para sair",
                          black, 50, size = "small")
        pygame.display.update()
        clock.tick(5)
        
                

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])
    

def tela_inicial():
    
    intro = True
    
    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
        
        
        
        gameDisplay.fill(blue)
        message_to_screen("Atrasados do Insper",
                          green, -100, size = "large1")
        message_to_screen("Sua meta no jogo é desviar dos carros e tentar",
                          black, 0, size = "little")
        message_to_screen("chegar ao Insper. Mas como é                  chegar no",
                          black, 20, size = "little")
        message_to_screen("                              impossível",
                          red, 20, size = "little")
        message_to_screen("horário seu real objetivo é chegar o mais",
                          black, 40, size = "little")
        message_to_screen("longe possível!!",
                          black, 60, size = "little")
                          
        message_to_screen("Pressione C para jogar, P para pausar e",
                          black, 140, size = "small")
        message_to_screen("Q para sair.",
                          black, 160, size = "small")
                          
        pygame.display.update()
        clock.tick(20)
                          


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)        
    elif size == "little":
        textSurface = littlefont.render(text, True, color)
    elif size == "large1":
        textSurface = large1font.render(text, True, color)
        
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = 250, 325+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():

    lead_x=200
    lead_y=550 
    
    Posi = [-50,-100,-175]    
    lista = [100,200,300]
    j= random.randint(0,2)
    ParedeX= lista [j]
    ParedeY= -100
    lead_y_change= 0
    score= 0
    
    k= random.randint(0,2)
    ParedeX_2= lista [k]
    ParedeY_2= -100


    gameExit = False
    gameOver = False
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(blue)
            message_to_screen("Game Over!", red, -50, size = "large")
            message_to_screen("Pressione C para jogar ou Q para sair", black, 0,
                              size = "small")
            message_to_screen("Score: "+str(score), black, 50, size = "medium")
            pygame.display.update()
        
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        
        if ParedeY>650:
            j= random.randint(0,2)
            ParedeX= lista [j]
            ParedeY= Posi [j]
              
               
            k= random.randint(0,2)
            ParedeX_2= lista [k]
            ParedeY_2= Posi [k]
               
        

        for event in pygame.event.get():
           if event.type==pygame.QUIT:         
               gameExit=True
           
           
           if event.type == pygame.KEYDOWN:
        
        
            for event in pygame.event.get():
                if event.type==pygame.QUIT:         
                    gameExit=True
             
               
            if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_LEFT:
                       if 100<lead_x<=300:
                           lead_x -=100
                       
                   elif event.key==pygame.K_RIGHT:
                           if 100<=lead_x<300:
                               lead_x +=100
                   elif event.key == pygame.K_p:
                                   pause()
                       
        ParedeY += lead_y_change
        ParedeY_2 +=lead_y_change
        gameDisplay.fill(green) 
        
        
        gameDisplay.blit(img2,[100,0,300,650]) #Rua          
        if int(score)%2 == 0 and int(score)%5 == 0:
            gameDisplay.blit(img,[lead_x, lead_y,100,100]) #Personagem
        elif int(score)%2 == 0:
            gameDisplay.blit(imgr,[lead_x, lead_y,100,100])
        else :
            gameDisplay.blit(imgl,[lead_x, lead_y,100,100])
        gameDisplay.blit(img3,[ParedeX,ParedeY,100,100]) # Carro
        gameDisplay.blit(img4,[ParedeX_2,ParedeY_2,100,100]) #Carro 2
        
        text = smallfont.render(" Score: ", True, black)
        gameDisplay.blit(text, [0,0])
        text = smallfont.render("  "+str(score), True, black)
        gameDisplay.blit(text, [0,20])    
    
        pygame.display.update()
        clock.tick(22+0.03*int(score))
        score+=1
        lead_y_change =+10

        

        if ParedeX+10 <= lead_x+10 < ParedeX+80 and ParedeY+10 <= lead_y+10 < ParedeY+110:
            gameOver = True
        if ParedeX+10 <= lead_x+70 < ParedeX+80 and ParedeY+10 <= lead_y+80 < ParedeY+110:
            gameOver = True
            
        if ParedeX_2+10 <= lead_x+10 < ParedeX_2+80 and ParedeY_2+10 <= lead_y+10 < ParedeY_2+110:
            gameOver = True
        if ParedeX_2+10 <= lead_x+70 < ParedeX_2+80 and ParedeY_2+10 <= lead_y+80 < ParedeY_2+110:
            gameOver = True	    
    
    pygame.quit()
    quit()

tela_inicial()
gameLoop()
