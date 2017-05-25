import pygame
import sys
import os
import Grid
import GUI
from MDP import MDP
from MPD_Analysis import MDPA


def game(dim, rock, fire, w, rew, discount):
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    x = 0
    y = 25
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    screen = pygame.display.set_mode((dim*w, dim*w))
    font = pygame.font.SysFont('monospace', 14)
    pygame.display.set_caption('Grid')
    screen.fill(white)
    Grid.grid_builder(dim, screen, blue)
    pygame.display.update()
    counter = 0
    rock_mat = []
    fire_mat = []

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and counter == rock + fire + 1:
                    gridInt = MDP(dim, rock_mat, fire_mat, treasure_site)
                    mapGrid = MDPA(dim, gridInt, rew, discount)

                    row_num = 0
                    col_num = 0

                    for row in mapGrid:
                        for col in row:
                            surfaceFont = font.render(col, True, black)
                            surfaceR = surfaceFont.get_rect()
                            surfaceR.center = ((col_num-1)*w + w / 2, (row_num-1)*w + w / 2)
                            screen.blit(surfaceFont, surfaceR)
                            col_num += 1
                        col_num = 0
                        row_num += 1

            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x_coord, y_coord) = pygame.mouse.get_pos()
                position_x = int(x_coord/w)
                position_y = int(y_coord/w)
                if counter == 0:
                    pygame.draw.rect(screen, green, [position_x*w+2, position_y*w+2, w-3, w-3])
                    treasure_site = [position_y, position_x]
                    counter += 1
                elif counter <= rock:
                    pygame.draw.rect(screen, black, [position_x*w+2, position_y*w+2, w-3, w-3])
                    rock_mat.append([position_y, position_x])
                    counter += 1
                elif counter <= rock + fire:
                    pygame.draw.rect(screen, red, [position_x*w+2, position_y*w+2, w-3, w-3])
                    fire_mat.append([position_y, position_x])
                    counter += 1
            pygame.display.update()

    screen.fill(white)
    pygame.display.update()
    GUI.main()
    pygame.quit()
    quit()
