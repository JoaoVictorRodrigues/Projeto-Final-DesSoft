import pygame
import random
pygame.init()


white=(255,255,255)
black=(0,0,0)
gray=(128,128,128)
blue=(0,0,255)

gameDisplay=pygame.display.set_mode((500,650))
pygame.display.set_caption("Atrasados do Insper")

pygame.display.update()

gameExit= False

lead_x=200
lead_y=550 

randParedeX= random.randrange(100,300)
ParedeY= 0

clock = pygame.time.Clock()
lead_y_change= 0

while not gameExit:
     for event in pygame.event.get():
        if event.type==pygame.QUIT:         
            gameExit=True
        
        if event.type == pygame.KEYDOWN:
           lead_y_change =+1
     
           if event.key == pygame.K_LEFT:
                if 100<lead_x<=300:
                    lead_x -=100
                    
           if event.key==pygame.K_RIGHT:
                if 100<=lead_x<300:
                    lead_x +=100
                    #lead_y_change =+10
            
     ParedeY += lead_y_change
     gameDisplay.fill(white) 
     #Rua 
     pygame.draw.rect(gameDisplay,gray,[100,0,300,650])
     #Personagem     
     pygame.draw.rect(gameDisplay,blue,[lead_x,lead_y,100,100])
     #Barreiras
     pygame.draw.rect(gameDisplay,black,[randParedeX,ParedeY,100,20])
     pygame.display.update()
     clock.tick(20)
     
pygame.quit()

quit()