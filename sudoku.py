import pygame
import os, sys
import random
import time

# Setup & Setup Variables
clock = pygame.time.Clock()
win = pygame.display.set_mode((600, 700))
pygame.display.set_caption = 'Sudoku'
pygame.font.init()
input_font = pygame.font.Font(None, 24)
user_input = ''
input_rect = pygame.Rect(10,10,20,20)

# Asset Loading
template = pygame.image.load(os.path.join("template1.jpg"))

#Main Game Function
def main():
    run = True
    global user_input

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if len(user_input) < 1:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
        
        win.fill((0, 0, 0))
        win.blit(template,(0,0))
        text_surface = input_font.render(user_input,True,(100,100,100))
        win.blit(text_surface,(input_rect.x + 5,input_rect.y + 2.5))

        pygame.draw.rect(win,pygame.Color('lightskyblue3'),input_rect,2)
        pygame.display.flip()
        clock.tick(60)
        
main()