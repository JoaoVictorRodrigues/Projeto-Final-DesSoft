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
img2 = pygame.image.load("C:\Rua2.png")
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

def menssage_to_screen(msg,cor):
    screen_text = font.render(msg, True, cor)
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])

while not gameExit:
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
     clock.tick(10)
     
message_to_screen("O João é Otário", red)     
pygame.display.update()
time.sleep(2)
     
pygame.quit()

quit()