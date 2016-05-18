import pygame
import random
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
img3 = pygame.image.load("C:\Carro.png")


pygame.display.update()

gameExit= False

lead_x=200
lead_y=550 

randParedeX= random.randrange(100,200)
#randParedeX2= random.randrange(220,300)
ParedeY= 0
lead_y_change= 0


while not gameExit:
     for event in pygame.event.get():
        if event.type==pygame.QUIT:         
            gameExit=True
        
        if ParedeY>600:
          randParedeX= random.randrange(100,300)
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
     gameDisplay.blit(img2,(100,50,350,650))        
     #Personagem     
     #pygame.draw.rect(gameDisplay,blue,[lead_x,lead_y,100,100])
     gameDisplay.blit(img, (lead_x,lead_y))
     #Barreiras
     #pygame.draw.rect(gameDisplay,black,[randParedeX,ParedeY,100,20])
     gameDisplay.blit(img3,[randParedeX,ParedeY,100,20])
    


     pygame.display.update()
     clock.tick(10)
     
pygame.quit()

quit()