import pygame

def algorithm(draw, grid, start, end):
    open_set, open_set_hash = [], []
    open_set.append(start)
    open_set_hash.append(start)
    cameFrom = {}

    while len(open_set) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
        current = open_set.pop(0)
        if current == end:
            return cameFrom
        for bro in current.bros:
            if bro not in open_set_hash:
                open_set_hash.append(bro)
                cameFrom[bro] = current
                open_set.append(bro)
                bro.makeOpen()
        draw()
        if current != start:
            current.makeClosed()
    return False
