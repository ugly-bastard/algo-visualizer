def algorithm(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst)):
        k = i
        for j in range(i+1, len(lst)):
            if (lst[k] > lst[j] and ascending) or (lst[k] < lst[j] and not ascending):
                k = j
            draw_info.draw_list({i: draw_info.GREEN,
                                 j: draw_info.RED,
                                 k: draw_info.GREEN}, True)
            yield True
        lst[i], lst[k] = lst[k], lst[i]

    return lst
