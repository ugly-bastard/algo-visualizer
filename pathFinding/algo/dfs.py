import pygame

def algorithm(draw, grid, start, end):
    open_set = []
    open_set_hash = []
    open_set.append(start)
    cameFrom = {}

    path = []

    current = open_set.pop(0)
    open_set.append(current)

    while (len(open_set)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
        current = open_set[-1]
        open_set.pop()
        if current == end:
            return cameFrom

        if current not in open_set_hash:
            path.append(current)
            open_set_hash.append(current)

        for bro in current.bros:
            # bro.makeOpen()
            if bro not in open_set_hash:
                cameFrom[bro] = current
                open_set.append(bro)
                open_set_hash.append(bro)
                if bro != end:
                    bro.makeOpen()
        draw()
        if current != start:
            current.makeClosed()

    return False
