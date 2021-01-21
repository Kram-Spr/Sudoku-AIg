import pygame
import os, sys
import random
import time

class Grid:
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def divide_board(self, win):
        gap = self.width / 9
        for i in range(self.row):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 2
            pygame.draw.line(win,(0,0,0), ((i * gap) - 1,0), ((i*gap) - 1,self.height), thickness)
            pygame.draw.line(win,(0,0,0), (0,(i * gap) - 1), (self.width,(i*gap) - 1), thickness)

def refresher(win):
    win.fill((255,255,255))
    Grid(9,9,600,600).divide_board(win)
    pygame.display.update()

def main():
    win = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Sudoku")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.time.Clock().tick(40)
        refresher(win)

main()