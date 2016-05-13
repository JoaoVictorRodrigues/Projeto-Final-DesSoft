import pygame
pygame.init()

white=(255,255,255)
gray=(128,128,128)
blue=(0,0,255)

gameDisplay=pygame.display.set_mode((500,650))
pygame.display.set_caption("Atrasados do Insper")
<<<<<<< HEAD

=======
>>>>>>> 80f0d325719feb67d5626fa375dc031f2b04307e

pygame.display.update()

gameExit= False

lead_x=200
lead_y=550
#lead_x_change= 0

clock = pygame.time.Clock()




while not gameExit:
     for event in pygame.event.get():
        if event.type==pygame.QUIT:         
            gameExit=True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
<<<<<<< HEAD
                lead_x -=100
            elif event.key==pygame.K_RIGHT:
                lead_x +=100
            elif event.key == pygame.K_LEFT:
                lead_x -=100
            elif event.key==pygame.K_RIGHT:
                lead_x +=100

=======
                if 100<lead_x<=300:
                    lead_x -=100  
            if event.key==pygame.K_RIGHT:
                if 100<=lead_x<300:
                    lead_x +=100
        
     
>>>>>>> 80f0d325719feb67d5626fa375dc031f2b04307e
     gameDisplay.fill(white) 
     pygame.draw.rect(gameDisplay,gray,[100,0,300,650])
     pygame.draw.rect(gameDisplay,blue,[lead_x,lead_y,100,100])
     
     pygame.display.update()
<<<<<<< HEAD

     clock.tick(10)
=======
     
>>>>>>> 80f0d325719feb67d5626fa375dc031f2b04307e
     
pygame.quit()
quit()