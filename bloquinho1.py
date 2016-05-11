# -*- coding: utf-8 -*-
import pygame

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()

gamedisplay = pygame.display.set_mode((500,700))
pygame.display.set_caption("sigiane lixo")

pygame.display.update()

gameexit = False

lead_x = 300
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()

while not gameexit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -2
            if event.key == pygame.K_RIGHT:
                lead_x_change = 2
    lead_x += lead_x_change
    gamedisplay.fill(white)
    pygame.draw.rect(gamedisplay, black, [lead_x, lead_y, 100, 100])
    pygame.display.update()

    clock.tick(100)

            
pygame.quit()

quit()