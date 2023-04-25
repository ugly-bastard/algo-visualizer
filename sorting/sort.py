import pygame
import random
import math
from tkinter import Tk, ttk
from sorting.algo import bubble, insertion, selection

class DrawInformation:
    pygame.init()
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


    def draw(self, algo_name, ascending):
        self.win.fill(self.BACKGROUND_COLOR)

        title = self.LARGE_FONT.render(
            f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
            True, self.GREEN
        )
        self.win.blit(title, (self.width/2 - title.get_width()/2 , 10))

        controls = self.FONT.render(
            "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending",
            True, self.BLACK
        )
        self.win.blit(controls, (self.width/2 - controls.get_width()/2 , 50))

        self.draw_list()
        pygame.display.update()


    def draw_list(self, color_positions={}, clear_bg=False):
        lst = self.lst

        if clear_bg:
            clear_rect = (self.SIDE_PAD//2, self.TOP_PAD, 
                            self.width - self.SIDE_PAD, self.height - self.TOP_PAD)
            pygame.draw.rect(self.win, self.BACKGROUND_COLOR, clear_rect)

        for i, val in enumerate(lst):
            x = self.start_x + i * self.block_width
            y = self.height - (val - self.min_val) * self.block_height

            color = self.GRADIENTS[i % 3]

            if i in color_positions:
                color = color_positions[i] 

            pygame.draw.rect(self.win, color, (x, y, self.block_width, self.height))

        if clear_bg:
            pygame.display.update()


def genList(lstLen, minVal, maxVal):
    lst = []

    for _ in range(lstLen):
        val = random.randint(minVal, maxVal)
        lst.append(val)

    return lst


def choice():
    algo=bubble
    algoName="Bubble Sort"
    def algorizzm(al, root):
        nonlocal algoName
        algoName=al
        root.destroy()

    root=Tk()
    root.attributes('-type', 'dialog')
    root.geometry("300x200")
    ttk.Button(root, text="Bubble Sort", width=20,
               command=lambda: algorizzm("Bubble Sort", root)
               ).pack(pady=20)
    ttk.Button(root, text="Insertion Sort", width=20,
               command=lambda: algorizzm("Insertion Sort", root)
               ).pack(pady=20)
    ttk.Button(root, text="Selection Sort", width=20,
               command=lambda: algorizzm("Selection Sort", root)
               ).pack(pady=20)
    root.mainloop()

    if algoName == "Bubble Sort":
        algo = bubble
    elif algoName == "Insertion Sort":
        algo = insertion
    elif algoName == "Selection Sort":
        algo = selection

    return algo, algoName

def main():
    run = True
    clock = pygame.time.Clock()

    lstLen = 50
    minVal = 0
    maxVal = 100

    lst = genList(lstLen, minVal, maxVal)
    draw_info = DrawInformation(800, 600, lst)
    sorting = False
    ascending = True

    algo = bubble
    algoName = "Sorting Algorithm"
    algoGen = None

    while run:
        clock.tick(60)
        if sorting:
            try: next(algoGen)
            except StopIteration:
                sorting = False
        else:
            draw_info.draw(algoName, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = genList(lstLen, minVal, maxVal)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_SPACE and sorting == False:
                algo, algoName = choice()
                draw_info.draw(algoName, ascending)
                sorting = True
                algoGen = algo.algorithm(draw_info, ascending)

    pygame.quit()


if __name__ == "__main__":
    main()
