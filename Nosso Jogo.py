import pygame
import random
import os
pygame.init()

red =(255,0,0)
white=(255,255,255)
black=(0,0,0)
gray=(128,128,128)
blue=(0,0,255)


clock = pygame.time.Clock()

gameDisplay=pygame.display.set_mode((500,650))
pygame.display.set_caption("Atrasados do Insper")
    

img = pygame.image.load("C:\Stickboy.png")
img2 = pygame.image.load("C:\Rua_2.png")
img3 = pygame.image.load("C:\Carro ferrari.png")

pygame.display.update()


gameExit= False



persoX= 100
persoY= 650

lead_x=300
lead_y=550 

j= random.randint(0,2)
lista = [100,200,300]
ParedeX= lista [j]

ParedeY= 0
lead_y_change= 0

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text,[250,325])

def gameLoop():

    lead_x=300
    lead_y=550 
    
    j= random.randint(0,2)
    lista = [100,200,300]
    ParedeX= lista [j]
    
    ParedeY= 0
    lead_y_change= 0

    gameExit = False
    gameOver = False
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
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
               ParedeY= 0  
           
           if event.type == pygame.KEYDOWN:
               lead_y_change =+10
        
               if event.key == pygame.K_LEFT:
                   if 100<lead_x<=300:
                       lead_x -=100
                       
               elif event.key==pygame.K_RIGHT:
                   if 100<=lead_x<300:
                       lead_x +=100
                       
                       
        ParedeY += lead_y_change
        gameDisplay.fill(white) 
        
        
        #Rua      
        #pygame.draw.rect(gameDisplay,gray,[100,0,300,650])
        gameDisplay.blit(img2,(100,0,300,650))        
        #Personagem     
        #pygame.draw.rect(gameDisplay,blue,[lead_x,lead_y,100,100])
        gameDisplay.blit(img,(lead_x, lead_y,100,100))
        #Barreiras
        #pygame.draw.rect(gameDisplay,black,[randParedeX,ParedeY,100,20])
        gameDisplay.blit(img3,[ParedeX,ParedeY,100,100])
    
    
    
        pygame.display.update()
        clock.tick(30)
         
#    largura_carro_x = 100
#    altura_carro_y = 100      
#         
#    x=100
#    y=100     
#         
#    
        if lead_x == ParedeX and lead_y == ParedeY or lead_x == ParedeX and ParedeY+50 == lead_y:
             gameOver = True
	
         
    
    pygame.quit()
    quit()
    
gameLoop()