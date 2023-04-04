import pygame
from tkinter import Tk, ttk, messagebox

# from algo import insertion sort, selection sort,\
# merge sort, quick brown fox jumps over the lazy dog (or not) sort

ROWS = 50
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A cool name")

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
TURQUOISE = (64,224,208)

def main(win, width):
    pygame.quit()

main(WIN, WIDTH)
