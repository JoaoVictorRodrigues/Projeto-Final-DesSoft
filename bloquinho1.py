# -*- coding: utf-8 -*-
import pygame



white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
verde = (0,255,0)
blue = (0,0,255)
display_width = 700
display_height = 500

pygame.init()

gamedisplay = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption("sigiane lixo")

pygame.display.update()

gameexit = False

lead_x = display_height/2
lead_y = display_height/2


clock = pygame.time.Clock()

while not gameexit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 100
            if event.key == pygame.K_RIGHT:
                lead_x += 100
    gamedisplay.fill(white)
    pygame.draw.rect(gamedisplay, black, [lead_x, lead_y, 100, 100])
    pygame.display.update()

    clock.tick(100)
    
font = pygame.font.Sysfont(None, 25)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gamedisplay.blit(screen_text, [display_width/2, display_height/2])
    
    
    
def tela_inicial():
    
    intro = True
    
    while intro:
        gamedisplay.fill(verde)
        message_to_screen("bem vindo ao ATRASADOS DO INSPER",
                          red,
                          -100,
                          "large")
        message_to_screen("seu objetivo nesse jogo é chegar no horario pra a aula de tutoria",
                          blue,
                          -30)
        pygame.display.update()
        clock.tick(15)
        


pygame.quit()

quit()