import pygame
import math
from queue import PriorityQueue

def algorithm(draw, grid, start, end):
    def h(p1, p2):
        x1,y1 = p1
        x2,y2 = p2
        return abs(x1-x2) + abs(y1-y2)
        # return math.sqrt((x1-x2)**2 + abs(y1-y2)**2)

    count= 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    cameFrom = {}
    g = {spot: float("inf") for row in grid for spot in row}
    g[start] = 0
    f = {spot: float("inf") for row in grid for spot in row}
    f[start] = h(start.getPos(), end.getPos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            return cameFrom
        for bro in current.bros:
            temp_g = g[current]+1
            if temp_g < g[bro]:
                cameFrom[bro] = current
                g[bro] = temp_g
                f[bro] = temp_g + h(bro.getPos(), end.getPos())
                if bro not in open_set_hash:
                    count+=1
                    open_set.put((f[bro], count, bro))
                    open_set_hash.add(bro)
                    bro.makeOpen()
        draw()
        if current != start:
            current.makeClosed()
    return False

