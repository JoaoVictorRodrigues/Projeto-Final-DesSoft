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
    

img = pygame.image.load("C:\Stickboy.png")
img2 = pygame.image.load("C:\Rua_2.png")
img3 = pygame.image.load("C:\Carro ferrari.png")
img4 = pygame.image.load("C:\carro verde.png")

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
        message_to_screen("chagar ao Inser. Mas como é                   chegar no",
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
        clock.tick(30)
                          


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

    lead_x=300
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
        
        for event in pygame.event.get():
           if event.type==pygame.QUIT:         
               gameExit=True
           
           
           if ParedeY>650:
               j= random.randint(0,2)
               ParedeX= lista [j]
               ParedeY= Posi [j]
              
               
               k= random.randint(0,2)
               ParedeX_2= lista [k]
               ParedeY_2= Posi [k]
               
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
        
        
        gameDisplay.blit(img2,(100,0,300,650)) #Rua          
        gameDisplay.blit(img,(lead_x, lead_y,100,100)) #Personagem
        gameDisplay.blit(img3,[ParedeX,ParedeY,100,100]) # Carro
        gameDisplay.blit(img4,[ParedeX_2,ParedeY_2,100,100]) #Carro 2
    
        text = smallfont.render(" Score: ", True, black)
        gameDisplay.blit(text, [0,0])
        text = smallfont.render("  "+str(score), True, black)
        gameDisplay.blit(text, [0,20])    
    
        pygame.display.update()
        clock.tick(20)
        score+=1
        lead_y_change =+10
        if lead_x == ParedeX and lead_y == ParedeY or lead_x == ParedeX and ParedeY+50 == lead_y or lead_y+90 == ParedeY and lead_x == ParedeX:
             gameOver = True
        if lead_x == ParedeX_2 and lead_y == ParedeY_2 or lead_x == ParedeX_2 and ParedeY_2+50 == lead_y or lead_y+90 == ParedeY_2 and lead_x == ParedeX_2:
             gameOver = True
	    
    
    pygame.quit()
    quit()

tela_inicial()
gameLoop()