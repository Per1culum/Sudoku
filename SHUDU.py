import random
from tkinter.messagebox import showinfo
import pygame
from pygame.color import THECOLORS as COLORS
from tkinter import *


# 数独数字范围（模块级常量，避免类方法硬依赖全局变量）
NUMBER_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class SudokuGame:
    """数独游戏核心逻辑：生成棋盘、校验规则、挖空。"""

    @staticmethod
    def print_matrix(matrix):
        """打印矩阵（调试用）。"""
        print('—' * 19)
        for row in matrix:
            print('|' + ' '.join([str(col) for col in row]) + '|')
        print('—' * 19)

    @staticmethod
    def shuffle_number(any_list):
        """打乱列表顺序。"""
        random.shuffle(any_list)
        return any_list

    @staticmethod
    def check(matrix, i, j, number):
        """检查在 (i, j) 位置填入 number 是否符合数独规则。"""
        if number in matrix[i]:
            return False
        if number in [row[j] for row in matrix]:
            return False
        part_i, part_j = i // 3, j // 3
        if number in [matrix[r][c]
                      for r in range(part_i * 3, (part_i + 1) * 3)
                      for c in range(part_j * 3, (part_j + 1) * 3)]:
            return False
        return True

    @staticmethod
    def build_map(matrix, i, j, number):
        """回溯法生成完整数独解。"""
        if i > 8 or j > 8:
            return matrix
        if SudokuGame.check(matrix, i, j, number):
            matrix_no1 = [[col for col in row] for row in matrix]
            matrix_no1[i][j] = number
            next_i, next_j = (i + 1, 0) if j == 8 else (i, j + 1)
            for number2 in SudokuGame.shuffle_number(list(NUMBER_LIST)):
                matrix_no2 = SudokuGame.build_map(matrix_no1, next_i, next_j, number2)
                if matrix_no2 and sum([sum(row) for row in matrix_no2]) == (sum(range(1, 10)) * 9):
                    return matrix_no2
        return None

    @staticmethod
    def prepare_game(blank_size=9):
        """生成游戏棋盘：完整解 + 挖空后的棋盘 + 空格坐标列表。"""
        matrix = [[0] * 9 for _ in range(9)]
        matrix_all = SudokuGame.build_map(matrix, 0, 0, random.choice(NUMBER_LIST))
        blank_positions = set()
        while len(blank_positions) < blank_size:
            i, j = random.randint(0, 8), random.randint(0, 8)
            blank_positions.add((i, j))
        matrix_blank = [[col for col in row] for row in matrix_all]
        blank_ij = []
        for i, j in blank_positions:
            blank_ij.append((i, j))
            matrix_blank[i][j] = 0
        return matrix_all, matrix_blank, blank_ij


def draw_bg():
    """绘制背景和九宫格线。"""
    BG_COLOR = (40, 40, 60)  # 背景色（黑蓝）
    screen.fill(BG_COLOR)
    pygame.display.set_caption('数独游戏')
    pygame.draw.rect(screen, COLORS['black'], (0, 0, 200, 600), 3)   # 竖线
    pygame.draw.rect(screen, COLORS['black'], (200, 0, 200, 600), 3)
    pygame.draw.rect(screen, COLORS['black'], (400, 0, 200, 600), 3)
    pygame.draw.rect(screen, COLORS['black'], (0, 0, 600, 200), 3)   # 横线
    pygame.draw.rect(screen, COLORS['black'], (0, 200, 600, 200), 3)
    pygame.draw.rect(screen, COLORS['black'], (0, 400, 600, 200), 3)


def draw_choose():
    """绘制选中方块的高亮。"""
    BLOCK_COLOR = (129, 216, 208)  # 蒂凡尼蓝
    pygame.draw.rect(screen, BLOCK_COLOR, (curJ * 66 + 5, curI * 66 + 5, 66 - 6, 66 - 6), 0)


def win_or_not(matrix_all, matrix):
    """判断是否获胜。"""
    return matrix_all == matrix


def check_color(matrix, i, j):
    """检查 (i, j) 位置的数字是否合规，返回对应颜色。"""
    matrix_no1 = [[col for col in row] for row in matrix]
    matrix_no1[i][j] = 0
    if SudokuGame.check(matrix_no1, i, j, matrix[i][j]):
        return COLORS['green']
    return COLORS['red']


def draw_num():
    """绘制棋盘上的所有数字。"""
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[0])):
            _color = check_color(MATRIX, i, j) if (i, j) in BLANK_IJ else COLORS['gray']
            txt = font.render(str(MATRIX[i][j] if MATRIX[i][j] not in [0, '0'] else ''), True, _color)
            x, y = j * 66 + 20, i * 66 + 6
            screen.blit(txt, (x, y))


def draw_context():
    """绘制底部信息栏。"""
    txt = font.render('Blank:' + str(cur_blank_size) + '   Change:' + str(cur_change_size), True, COLORS['white'])
    x, y = 10, 600
    screen.blit(txt, (x, y))


def level(number):
    """设置难度并关闭选择窗口。"""
    global cur_blank_size, root
    cur_blank_size = number
    root.destroy()


def startgame():
    """显示难度选择窗口。"""
    global root
    root = Tk()
    root.title("数独游戏")
    Label(root, text="欢迎来到数独游戏，请选择难度").place(x=60, y=1)
    root.geometry("300x120")
    button0 = Button(root, text="简单", width=8, command=lambda: level(10))
    button1 = Button(root, text="一般", width=8, command=lambda: level(25))
    button2 = Button(root, text="困难", width=8, command=lambda: level(35))
    button3 = Button(root, text="大师", width=8, command=lambda: level(55))
    button0.place(x=10, y=40)
    button1.place(x=80, y=40)
    button2.place(x=150, y=40)
    button3.place(x=220, y=40)
    root.mainloop()


if __name__ == "__main__":
    pygame.init()
    cur_blank_size = 10
    startgame()

    SIZE = [600, 700]  # 窗口尺寸
    font = pygame.font.SysFont('Times', 50)

    screen = pygame.display.set_mode(SIZE)

    curI, curJ = 0, 0
    cur_change_size = 0

    # 生成游戏棋盘
    MATRIX_ANSWER, MATRIX, BLANK_IJ = SudokuGame.prepare_game(blank_size=cur_blank_size)
    SudokuGame.print_matrix(MATRIX)

    # 小键盘键码映射
    KEYPAD_MAP = {
        pygame.K_KP1: 1, pygame.K_KP2: 2, pygame.K_KP3: 3,
        pygame.K_KP4: 4, pygame.K_KP5: 5, pygame.K_KP6: 6,
        pygame.K_KP7: 7, pygame.K_KP8: 8, pygame.K_KP9: 9,
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_j, click_i = int(event.pos[0] / 66), int(event.pos[1] / 66)
                # 边界检查：只允许点击 9x9 棋盘区域
                if 0 <= click_i < 9 and 0 <= click_j < 9:
                    curI, curJ = click_i, click_j
            elif event.type == pygame.KEYUP:
                # 解析输入数字：主键盘 1-9 或小键盘 KP1-KP9
                input_num = None
                if pygame.K_1 <= event.key <= pygame.K_9:
                    input_num = event.key - pygame.K_0
                elif event.key in KEYPAD_MAP:
                    input_num = KEYPAD_MAP[event.key]

                if input_num is not None and (curI, curJ) in BLANK_IJ:
                    MATRIX[curI][curJ] = input_num
                    cur_blank_size = sum(1 for row in MATRIX for col in row if col == 0)
                    cur_change_size += 1

        draw_bg()
        draw_choose()
        draw_num()
        draw_context()
        pygame.display.flip()

        if win_or_not(MATRIX_ANSWER, MATRIX):
            showinfo(title="Game end", message="You win, well done!")
            break

    pygame.quit()
