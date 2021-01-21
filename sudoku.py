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
        self.current_x = 5
        self.current_y = 5
        self.grids = []
        self.runs = 0
        
    def divide_board(self, win):
        space = self.width / 9
        for i in range(self.row + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 2
            pygame.draw.line(win,(0,0,0), (i * space,0), (i*space,self.height), thickness)
            pygame.draw.line(win,(0,0,0), (0,i * space), (self.width,i*space), thickness)
            if i % 9 == 0:
                pygame.draw.line(win,(0,0,0), (0,i * space), (self.width,i*space), 10)
        
        for i,r in enumerate(self.board, start=0):
            for o,c in enumerate(r,start=0):
                self.runs += 1
                current_rect = pygame.Rect((self.current_x, self.current_y),(60,60))
                grid = pygame.draw.rect(win, (220,50,50), current_rect)

                if self.runs <= 81:
                    self.grids.append(str(grid))
                    print(self.grids)
            
                if o >= 8 and (i + 1) % 3 != 0:
                    self.current_x = 6
                    self.current_y += 65
                elif o >= 8 and (i + 1) % 3 == 0:
                    self.current_x = 6
                    self.current_y += 70
                else:
                    if (o + 1) % 3 == 0 and o != 0:
                        self.current_x += 70
                        self.current_y += 0
                    else:
                        self.current_x += 65
                        self.current_y += 0
    
    #def create_rect_inputs(self, win):
        #pass
    
def solver_activate(self):
    pass

def refresher(win):
    win.fill((255,255,255))
    full_board = Grid(9,9,600,600)
    full_board.divide_board(win)
    #full_board.create_rect_inputs(win)
    pygame.display.update()

def main():
    win = pygame.display.set_mode((600,700))
    pygame.display.set_caption("Sudoku")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.time.Clock().tick(40)
        mouse_pos = pygame.mouse.get_pos()

        #print(mouse_pos)
        refresher(win)

main()