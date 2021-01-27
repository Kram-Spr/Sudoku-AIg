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
        
    def divide_board(self, win):
        pygame.font.init()

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
                current_rect = pygame.Rect((self.current_x, self.current_y),(60,60))
                grid = pygame.draw.rect(win, (255,255,255), current_rect)
            
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

                current_font = pygame.font.SysFont('Arial', 30)
                if str(c) == '0':
                    c = ''
                current_text = current_font.render(str(c), True, (0,0,0))
                win.blit(current_text, (grid.x + 20, grid.y + 10))

    def valid_input(self, input, rownum, colnum):
        valid = True

        for rn in self.board[rownum]:
            if rn == input:
                valid = False
        
        for r,rv in enumerate(self.board):
            if rv[colnum] == input:
                valid = False
        
        for row in range(0, 9, 3):
            for col in range(0,9,3):
                temp = []
                for r in range(row,row+3):
                    for c in range(col, col+3):
                        if self.board[r][c] != 0:
                            temp.append(self.board[r][c])
                if len(temp) != len(set(temp)):
                    valid = False

        return valid

    def find_empty(self):
        for i,r in enumerate(self.board, start=0):
            for o,c in enumerate(r, start=0):
                if self.board[i][o] == 0:
                    return (i,o)

    def solver_activate(self, win):
        found = self.find_empty()
        if not found:
            return True
        else:
            row,col = found

        for x in range(1,10): 
            if self.valid_input(x, row, col):
                refresher(win)
                pygame.time.delay(50)

                self.board[row][col] = x

                if self.solver_activate(win):
                    return True

                self.board[row][col] = 0

        return False

solve_button = ''

def refresher(win):
    global solve_button
    global full_board
    win.fill((255,255,255))
    full_board = Grid(9,9,600,600)
    full_board.divide_board(win)
    solve_rect = pygame.Rect((201, 615),(200,75))
    solve_button = pygame.draw.rect(win, (34,139,34), solve_rect)
    solve_font = pygame.font.SysFont('Arial', 30)
    solve_font.set_bold(True)
    solve_text = solve_font.render('SOLVE', True, (255,255,255))
    win.blit(solve_text, (solve_button.x + 50, solve_button.y + 15))
    pygame.display.update()

def main():
    global solve_button
    debounce = False
    win = pygame.display.set_mode((600,700))
    pygame.display.set_caption("Sudoku Solver")
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] > solve_button.x and mouse_pos[0] < (solve_button.x + 200) and mouse_pos[1] > solve_button.y and mouse_pos[1] < (solve_button.y + 75) and not debounce:
                    Grid(9,9,600,600).solver_activate(win)

        pygame.time.Clock().tick(30)
        refresher(win)

main()