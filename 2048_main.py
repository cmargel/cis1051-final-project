# sources:
#https://www.youtube.com/watch?v=HTJCUBp_S2I
#https://www.youtube.com/watch?v=qwJ9w5bmKZU&t=1744s
#https://www.youtube.com/watch?v=u2y06AOqKHc
#https://pythonprogramming.net/pygame-python-3-part-1-intro/


import random as r
import pygame
import sys

def printGrid(grid):
    print('-'*10)
    for row in grid:
        print(*row)
    print('-'*10)

def drawDisplay(score, change_score=0):
    pygame.draw.rect(screen, WHITE, REC)
    font = pygame.font.SysFont("stxingkai", 70)  
    font_score = pygame.font.SysFont("simaun", 48)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render(f"{score}", True, COLOR_TEXT)
    font_win = pygame.font.SysFont("simuan", 48)
    text_win = font_win.render("You win!", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value,(175,35))
    if win(grid) == True:
        screen.blit(text_win, (275, 35))
    if change_score > 0:
        text_change_score = font_score.render(f"+{change_score}", True, COLOR_TEXT)
        screen.blit(text_change_score, (170, 65))
    printGrid(grid)

    for row in range(BLOCKS):
        for col in range(BLOCKS):
            value = grid[row][col]
            text = font.render(f'{value}',True,BLACK) 
            w = col*SIZE_BLOCK + (col+1)*MARGIN
            h = row*SIZE_BLOCK + (row+1)*MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w,h,SIZE_BLOCK,SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK-font_w)/2
                text_y = h + (SIZE_BLOCK-font_h)/2
                screen.blit(text, (text_x, text_y))

def getNum(i, j):
    return i*4+j+1

def getIndex(num):
    num -= 1
    x,y = num//4, num%4
    return x,y

def addNewNum(grid,x,y):
    if r.random() <= 0.75:
        grid[x][y] = 2
    else:
        grid[x][y] = 4
    return grid

def getZeroes(grid):
    zeroes = []
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                num = getNum(i,j)
                zeroes.append(num)
    return zeroes

def win(grid):
    for row in grid:
        if 2048 in row:
            return True
    return False

def zero_in_grid(grid):
    for row in grid:
        if 0 in row:
            return True
    return False

def move_left(grid):
    change_score = 0
    for row in grid:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] *= 2
                change_score += grid[i][j]
                grid[i].pop(j+1)
                grid[i].append(0)
    return grid, change_score

def move_right(grid):
    change_score = 0
    for row in grid:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0,0)
    for i in range(4):
        for j in range(3, 0, -1):
            if grid[i][j] == grid[i][j-1] and grid[i][j] != 0:
                grid[i][j] *= 2
                change_score += grid[i][j]
                grid[i].pop(j-1)
                grid[i].insert(0,0)
    return grid, change_score

def move_up(grid):
    change_score = 0
    for j in range(4):
        col = []
        for i in range(4):
            if grid[i][j] != 0:
                col.append(grid[i][j])
        while len(col) != 4:
            col.append(0)
        for i in range(3):
            if col[i] == col[i+1] and col[i] != 0:
                col[i] *=2 
                change_score += grid[i][j]
                col.pop(i+1)
                col.append(0)
        for i in range(4):
            grid[i][j] = col[i]
    return grid, change_score

def move_down(grid):
    change_score = 0
    for j in range(4):
        col = []
        for i in range(4):
            if grid[i][j] != 0:
                col.append(grid[i][j])
        while len(col) != 4:
            col.insert(0,0)
        for i in range(3,0,-1):
            if col[i] == col[i-1] and col[i] != 0:
                col[i] *= 2
                change_score += grid[i][j]
                col.pop(i-1)
                col.insert(0,0)
        for i in range(4):
            grid[i][j] = col[i]
    return grid, change_score


def can_move(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
                return True
    return False            


grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

COLOR_TEXT = (255, 127, 0)
COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 219),
    4: (240, 226, 202),
    8: (242, 177, 121),
    16: (236, 141, 85),
    32: (250, 123, 92),
    64: (234, 90, 56),
    128: (237, 207, 114),
    256: (242, 208, 75),
    512: (237, 207, 114),
    1024: (227, 186, 19),
    2048: (236, 192, 2),
    4096: (204, 204, 0),
    8192: (153, 153, 0),
    16384: (102, 102, 0)

}


WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS*SIZE_BLOCK + (BLOCKS+1)*MARGIN
HEIGHT = WIDTH+110
REC = pygame.Rect(0,0,WIDTH,110)
score = 0

#grid[1][2] = 2
#grid[3][0] = 4
#print(getZeroes(grid))
printGrid(grid)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
drawDisplay(score)
pygame.display.update()
while zero_in_grid(grid) or can_move(grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            change_score = 0
            if event.key == pygame.K_LEFT:
                grid, change_score = move_left(grid)
            elif event.key == pygame.K_RIGHT:
                grid, change_score = move_right(grid)
            elif event.key == pygame.K_UP:
                grid, change_score = move_up(grid)
            elif event.key == pygame.K_DOWN:
                grid, change_score = move_down(grid)
            score += change_score
            drawDisplay(score)
            zeroes = getZeroes(grid)
            r.shuffle(zeroes)
            r_num = zeroes.pop()
            x, y = getIndex(r_num)
            grid = addNewNum(grid, x, y)
            print(r_num)
            drawDisplay(score, change_score)
            pygame.display.update()



