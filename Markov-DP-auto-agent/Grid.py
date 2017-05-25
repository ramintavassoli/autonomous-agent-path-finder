import pygame


def grid_builder(dimension, display, color):

    s, r = 0, 0
    w = 60
    temp_grid = [[1] * dimension for n in range(dimension)]
    for row in temp_grid:
        for col in row:
            pygame.draw.rect(display, color,[s, r, w, w],2)
            s += w
        r += w
        s = 0
