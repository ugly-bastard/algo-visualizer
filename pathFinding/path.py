import pygame
from tkinter import Tk, ttk, messagebox

from algo import Astar, dijkstra, dfs


BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (128,128,128)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
TURQUOISE = (64,224,208)

class Spot:
    def __init__(self, row, col, width) -> None:
        self.row = row
        self.col = col
        self.color = WHITE
        self.bros = []
        self.previous = None
        self.width = width

    def getPos(self):
        return self.row, self.col

    def isBarrier(self):
        return self.color == BLACK

    def reset(self):
        self.color = WHITE

    def makeClosed(self):
        self.color = RED

    def makeOpen(self):
        self.color = GREEN

    def makeBarrier(self):
        self.color = BLACK

    def makeStart(self):
        self.color = ORANGE

    def makeEnd(self):
        self.color = TURQUOISE

    def makePath(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.row*self.width, self.col*self.width, self.width, self.width))

    def addNeighbours(self, grid):
        # self.bros = []
        if self.row > 0 and not grid[self.row][self.col-1].isBarrier():
            self.bros.append(grid[self.row][self.col-1])

        if self.row < ROWS-1 and not grid[self.row+1][self.col].isBarrier():
            self.bros.append(grid[self.row+1][self.col])

        if self.col < ROWS-1 and not grid[self.row][self.col+1].isBarrier():
            self.bros.append(grid[self.row][self.col+1])

        if self.row > 0 and not grid[self.row-1][self.col].isBarrier():
            self.bros.append(grid[self.row-1][self.col])

class Working:
    def __init__(self, ROWS, WIDTH) -> None:
        self.rows = ROWS
        self.width = WIDTH
        self.gap = WIDTH//ROWS
        self.win = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("Path Finding Visualizer")

    def makeGrid(self):
        grid = []
        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                spot = Spot(i, j, self.gap)
                grid[i].append(spot)

        return grid

    def drawGrid(self):
        for i in range(self.rows):
            pygame.draw.line(self.win, GREY, (0,i*self.gap), (self.width,i*self.gap))
            for j in range(self.rows):
                pygame.draw.line(self.win, GREY, (j*self.gap,0), (j*self.gap,self.width))

    def draw(self, grid):
        self.win.fill(WHITE)

        for row in grid:
            row[0].makeBarrier()
            row[self.rows-1].makeBarrier()
            for spot in row:
                if grid.index(row) in [0,self.rows-1]:
                    spot.makeBarrier()
                spot.draw(self.win)

        self.drawGrid()
        pygame.display.update()

    def getClickedPos(self, pos):
        y,x = pos

        row = y//self.gap
        col = x//self.gap

        return row,col

    def reconstructPath(self, cameFrom, current, draw):
        while current in cameFrom:
            current = cameFrom[current]
            current.makePath()
            draw()

    def choice(self):
        algo=Astar
        def algorizzm(al, root):
            nonlocal algo
            algo=al
            root.destroy()

        root=Tk()
        root.attributes('-type', 'dialog')
        root.geometry("300x200")
        ttk.Button(root, text="AStar", width=20,
                   command=lambda: algorizzm("AStar", root)
                   ).pack(pady=20)
        ttk.Button(root, text="Dijkstra", width=20,
                   command=lambda: algorizzm("dijkstra", root)
                   ).pack(pady=20)
        ttk.Button(root, text="DFS", width=20,
                   command=lambda: algorizzm("dfs", root)
                   ).pack(pady=20)
        root.mainloop()

        if algo == "AStar":
            algo = Astar
        elif algo == "dijkstra":
            algo = dijkstra
        elif algo == "dfs":
            algo = dfs

        return algo

    def main(self):
        grid = self.makeGrid()

        start = None
        end = None

        run = True

        while run:
            self.draw(grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row,col = self.getClickedPos(pos)
                    spot = grid[row][col]
                    if not start and spot != end:
                        start = spot
                        start.makeStart()
                    elif not end and spot != start:
                        end = spot
                        end.makeEnd()
                    elif spot != start and spot != end:
                        spot.makeBarrier()

                if pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    row,col = self.getClickedPos(pos)
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start and end:
                        for row in grid:
                            for spot in row:
                                spot.addNeighbours(grid)

                        algo = self.choice()
                        for row in grid:
                            for spot in row:
                                if not spot.isBarrier():
                                    if spot not in [start, end]:
                                        spot.reset()
                        cameFrom = algo.algorithm(lambda: self.draw(grid), grid, start, end)
                        if cameFrom is None:
                            exit(0)
                        elif cameFrom:
                            self.reconstructPath(cameFrom, end, lambda: self.draw(grid))
                            start.makeStart()
                            end.makeEnd()
                        else:
                            Tk().wm_withdraw()
                            messagebox.showinfo("No solution.", "There was no solution.")

                    if event.key == pygame.K_c:
                        start = None
                        end = None
                        grid = self.makeGrid()

        pygame.quit()

ROWS = 50
WIDTH = 500
work = Working(ROWS, WIDTH)
work.main()
