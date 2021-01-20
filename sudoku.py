import pygame
import os, sys
import random
import time

clock = pygame.time.Clock()
win = pygame.display.set_mode((750, 600))
pygame.display.set_caption = 'Sudoku'
pygame.font.init()
input_font = pygame.font.Font(None, 32)
user_input = ''

def main():
    run = True
    global user_input

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
        
        win.fill((0, 0, 0))
        text_surface = input_font.render(user_input,True,(255,255,255))
        win.blit(text_surface,(0,0))

        pygame.display.flip()
        clock.tick(60)
main()