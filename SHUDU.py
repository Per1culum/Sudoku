import random
from tkinter.messagebox import showinfo
import pygame
from pygame.color import THECOLORS as COLORS
from tkinter import *


class BUILAGAME():
    def __init__(self, matrix):
        self.matrix = matrix

    def PrintMatrix(matrix):
        print('—'*19)
        for row in matrix:
            print('|'+' '.join([str(col) for col in row])+'|')
        print('—'*19)


    def ShuffleNumber(AnyList):
        random.shuffle(AnyList)
        return AnyList


    def Check(matrix, i, j, number):
        if number in matrix[i]:
            return False
        if number in [row[j] for row in matrix]:
            return False
        pratI, pratJ = int(i/3), int(j/3)
        if number in [matrix[i][j] for i in range(pratI*3, (pratI+1)*3) for j in range(pratJ*3, (pratJ+1)*3)]:
            return False
        return True


    def BuildMap(matrix, i, j, number):
        if i > 8 or j > 8:
           return matrix
        if BUILAGAME.Check(matrix, i, j, number):
            mattrix_no1 = [[col for col in row] for row in matrix]
            mattrix_no1[i][j] = number
            next_i,next_j = (i+1, 0) if j == 8 else (i, j+1)
            for number2 in BUILAGAME.ShuffleNumber(number_list):
                mattrix_no2 = BUILAGAME.BuildMap(mattrix_no1, next_i, next_j, number2)
                if mattrix_no2 and sum([sum(row) for row in mattrix_no2]) == (sum(range(1, 10))*9):
                    return mattrix_no2
        return None


    def PreaGame(blank_size=9):
        matrix_all = BUILAGAME.BuildMap(matrix, 0, 0, random.choice(number_list))
        set_ij = set()
        while len(list(set_ij)) < blank_size:
            templist = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            set_ij.add(str(random.choice(templist))+','+str(random.choice(templist)))
        matrix_blank = [[col for col in row] for row in matrix_all]
        blank_ij = []
        for ij in list(set_ij):
            i,j = int(ij.split(',')[0]),int(ij.split(',')[1])
            blank_ij.append((i, j))
            matrix_blank[i][j] = 0
        return matrix_all, matrix_blank, blank_ij


def DrawBG():
    BG_COLOR = (40, 40, 60)  # 背景色（黑蓝）
    screen.fill(BG_COLOR)
    pygame.display.set_caption('数独游戏')
    pygame.draw.rect(screen, COLORS['black'], (0, 0, 200, 600), 3)#画出九宫格
    pygame.draw.rect(screen, COLORS['black'], (200, 0, 200, 600), 3)
    pygame.draw.rect(screen, COLORS['black'], (400, 0, 200, 600), 3)
    pygame.draw.rect(screen, COLORS['black'], (0, 0, 600, 200), 3)
    pygame.draw.rect(screen, COLORS['black'], (0, 200, 600, 200), 3)
    pygame.draw.rect(screen, COLORS['black'], (0, 400, 600, 200), 3)


def DrawChoose():
    BLOCK_COLOR = (129, 216, 208)  #选中方块颜色（蒂凡尼蓝）
    pygame.draw.rect(screen, BLOCK_COLOR, (curJ * 66 + 5, curI * 66 + 5, 66 - 6, 66 - 6), 0)


def WinorNot(matrix_all, matrix):
    if matrix_all == matrix:
        return True
    return False


def CheckColor(matrix, i, j):
    mattrix_no1 = [[col for col in row] for row in matrix]
    mattrix_no1[i][j] = 0
    if BUILAGAME.Check(mattrix_no1, i, j, matrix[i][j]):
        return COLORS['green']
    return COLORS['red']


def DrawNum():
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[0])):
            _color = CheckColor(MATRIX, i, j) if (i, j) in BLANK_IJ else COLORS['gray']
            txt = font80.render(str(MATRIX[i][j] if MATRIX[i][j] not in [0, '0'] else ''), True, _color)
            x, y = j * 66 + 20, i * 66 + 6       #字体占据大小
            screen.blit(txt, (x, y))


def DrawContext():
    txt = font100.render('Blank:' + str(cur_blank_size) + '   Change:' + str(cur_change_size), True, COLORS['white'])
    x, y = 10, 600
    screen.blit(txt, (x, y))

def level(number):
    global cur_blank_size
    cur_blank_size = number
    return

def startgame():
    root = Tk();
    root.title("数独游戏")
    Label(root, text="欢迎来到数独游戏，请选择难度").place(x=60, y=1)
    root.geometry("300x120")
    button0 = Button(root, text="简单", width=8, command=lambda: level(10))
    button1 = Button(root, text="一般", width=8, command=lambda: level(25))
    button2 = Button(root, text="困难", width=8, command=lambda: level(35))
    button3 = Button(root, text="大师", width=8, command=lambda: level(64))
    button0.place(x=10, y=40)
    button1.place(x=80, y=40)
    button2.place(x=150, y=40)
    button3.place(x=220, y=40)
    mainloop()


if __name__ == "__main__":
    pygame.init()
    cur_blank_size = 10
    startgame()
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    matrix = [([0] * 9) for i in range(9)]
    SIZE = [600, 700]#窗口尺寸
    font80 = pygame.font.SysFont('Times', 50)#字体大小
    font100 = pygame.font.SysFont('Times', 50)

    screen = pygame.display.set_mode(SIZE)

    curI, curJ = 0, 0
    cur_change_size = 0

    # matrix abount
    MATRIX_ANSWER, MATRIX, BLANK_IJ = BUILAGAME.PreaGame(blank_size=cur_blank_size)
    print(BLANK_IJ)
    BUILAGAME.PrintMatrix(MATRIX)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                curJ, curI = int(event.pos[0] / 66), int(event.pos[1] / 66)
            elif event.type == event.type == pygame.KEYUP:
                if chr(event.key) in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and (curI, curJ) in BLANK_IJ:
                    MATRIX[curI][curJ] = int(chr(event.key))
                    cur_blank_size = sum([1 if col == 0 or col == '0' else 0 for row in MATRIX for col in row])
                    cur_change_size += 1
        DrawBG()
        DrawChoose()
        DrawNum()
        DrawContext()
        pygame.display.flip()
        if WinorNot(MATRIX_ANSWER, MATRIX):
            showinfo(title="Game end", message="You win, well done!")
            break
    pygame.quit()