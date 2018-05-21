from pieces import Queen
from pieces import King
from pieces import Rock
from pieces import Knight
from pieces import Bishop
from pieces import Pawn
from UnoMove import Move
import sys
import pygame

def change_move(k):
    k.whose_move='black' if k.whose_move=='white' else 'white'
def get_pos(x, y):
    '''
    gets position by place on the board
    :param x:
    :param y:
    :return:
    '''
    y1 = 1 + (7 - ord(y) + ord('A'))
    return (10 + (x - 1) * 90, 10 + (y1) * 90)


def draw_bishop(col, screen, num):
    if col['bishops'][num].x > 1000:
        return None
    if col['bishops'][num].colour == 'white':
        colour = (255, 255, 255)
    else:
        colour = (10, 10, 10)

    coords = get_pos(col['bishops'][num].x, col['bishops'][num].y)

    if col['bishops'][num].colour == 'white':
        pygame.draw.polygon(screen, (0, 0, 0), [(coords[0] + 10, coords[1]), (coords[0] + 25, coords[1] - 70),
                                                (coords[0] + 65, coords[1] - 70),
                                                (coords[0] + 80, coords[1])], 2)
        pygame.draw.polygon(screen, (0, 0, 0), [(coords[0] + 10, coords[1] - 75), (coords[0] + 80, coords[1] - 75),
                                                (coords[0] + 80, coords[1] - 60),
                                                (coords[0] + 10, coords[1] - 60)], 2)
        pygame.draw.polygon(screen, (0, 0, 0), [(coords[0] + 15, coords[1] - 75), (coords[0] + 15, coords[1] - 85),
                                                (coords[0] + 20, coords[1] - 85),
                                                (coords[0] + 20, coords[1] - 75)], 2)
        pygame.draw.polygon(screen, (0, 0, 0), [(coords[0] + 32, coords[1] - 75), (coords[0] + 32, coords[1] - 85),
                                                (coords[0] + 37, coords[1] - 85),
                                                (coords[0] + 37, coords[1] - 75)], 2)
        pygame.draw.polygon(screen, (0, 0, 0), [(coords[0] + 55, coords[1] - 75), (coords[0] + 55, coords[1] - 85),
                                                (coords[0] + 60, coords[1] - 85),
                                                (coords[0] + 60, coords[1] - 75)], 2)
        pygame.draw.polygon(screen, (0, 0, 0), [(coords[0] + 70, coords[1] - 75), (coords[0] + 70, coords[1] - 85),
                                                (coords[0] + 75, coords[1] - 85),
                                                (coords[0] + 75, coords[1] - 75)], 2)
    pygame.draw.polygon(screen, colour, [(coords[0] + 10, coords[1]), (coords[0] + 25, coords[1] - 70),
                                         (coords[0] + 65, coords[1] - 70),
                                         (coords[0] + 80, coords[1])])
    pygame.draw.polygon(screen, colour, [(coords[0] + 10, coords[1] - 75), (coords[0] + 80, coords[1] - 75),
                                         (coords[0] + 80, coords[1] - 60),
                                         (coords[0] + 10, coords[1] - 60)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 15, coords[1] - 75), (coords[0] + 15, coords[1] - 85),
                                         (coords[0] + 20, coords[1] - 85),
                                         (coords[0] + 20, coords[1] - 75)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 32, coords[1] - 75), (coords[0] + 32, coords[1] - 85),
                                         (coords[0] + 37, coords[1] - 85),
                                         (coords[0] + 37, coords[1] - 75)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 55, coords[1] - 75), (coords[0] + 55, coords[1] - 85),
                                         (coords[0] + 60, coords[1] - 85),
                                         (coords[0] + 60, coords[1] - 75)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 70, coords[1] - 75), (coords[0] + 70, coords[1] - 85),
                                         (coords[0] + 75, coords[1] - 85),
                                         (coords[0] + 75, coords[1] - 75)])


def draw_knight(col, screen, num):
    if col['knights'][num].x > 1000:
        return None
    if col['knights'][num].colour == 'white':
        colour = (255, 255, 255)
        colour1 = (225, 225, 225)
    else:
        colour = (10, 10, 10)
        colour1 = (30, 30, 30)
    super_colour = (0, 0, 0)
    coords = get_pos(col['knights'][num].x, col['knights'][num].y)
    if col['knights'][num].colour == 'white':
        pygame.draw.ellipse(screen, super_colour, (coords[0] + 10, coords[1] - 60, 70, 40), 5)
        pygame.draw.ellipse(screen, super_colour, (coords[0] + 60, coords[1] - 80, 10, 40), 3)
        pygame.draw.ellipse(screen, super_colour, (coords[0] + 60, coords[1] - 80, 20, 10), 3)
        pygame.draw.ellipse(screen, super_colour, (coords[0] + 10, coords[1] - 50, 10, 40), 3)
        pygame.draw.rect(screen, super_colour, pygame.Rect(coords[0] + 25, coords[1] - 40, 8, 40), 3)
        pygame.draw.rect(screen, super_colour, pygame.Rect(coords[0] + 55, coords[1] - 40, 8, 40), 3)
    pygame.draw.ellipse(screen, colour, (coords[0] + 10, coords[1] - 60, 70, 40))
    pygame.draw.ellipse(screen, colour, (coords[0] + 60, coords[1] - 80, 10, 40))
    pygame.draw.ellipse(screen, colour, (coords[0] + 60, coords[1] - 80, 20, 10))
    pygame.draw.ellipse(screen, colour1, (coords[0] + 10, coords[1] - 50, 10, 40))
    pygame.draw.rect(screen, colour, pygame.Rect(coords[0] + 25, coords[1] - 40, 8, 40))
    pygame.draw.rect(screen, colour, pygame.Rect(coords[0] + 55, coords[1] - 40, 8, 40))


def draw_king(col, screen):
    if col['king'].x > 1000:
        return None
    if col['king'].colour == 'white':
        colour = (255, 255, 255)
    else:
        colour = (10, 10, 10)
    super_colour = (0, 0, 0)
    coords = get_pos(col['king'].x, col['king'].y)
    if col['king'].colour == 'white':
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 15, coords[1] - 10), (coords[0] + 15, coords[1] - 80),
                                                   (coords[0] + 45, coords[1] - 10)], 2)
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 35, coords[1] - 10), (coords[0] + 50, coords[1] - 80),
                                                   (coords[0] + 65, coords[1] - 10)], 2)
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 55, coords[1] - 10), (coords[0] + 85, coords[1] - 80),
                                                   (coords[0] + 85, coords[1] - 10)], 2)

    pygame.draw.polygon(screen, colour, [(coords[0] + 15, coords[1] - 10), (coords[0] + 15, coords[1] - 80),
                                         (coords[0] + 45, coords[1] - 10)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 35, coords[1] - 10), (coords[0] + 50, coords[1] - 80),
                                         (coords[0] + 65, coords[1] - 10)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 55, coords[1] - 10), (coords[0] + 85, coords[1] - 80),
                                         (coords[0] + 85, coords[1] - 10)])


def draw_queen(col, screen):
    if col['queen'].x > 1000:
        return None
    if col['queen'].colour == 'white':
        colour = (255, 255, 255)
    else:
        colour = (10, 10, 10)
    super_colour = (0, 0, 0)
    coords = get_pos(col['queen'].x, col['queen'].y)
    if col['queen'].colour == 'white':
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 29, coords[1] - 40), (coords[0] + 29, coords[1] - 80),
                                                   (coords[0] + 44, coords[1] - 40)], 3)
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 34, coords[1] - 40), (coords[0] + 49, coords[1] - 80),
                                                   (coords[0] + 64, coords[1] - 40)], 3)
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 54, coords[1] - 40), (coords[0] + 69, coords[1] - 80),
                                                   (coords[0] + 69, coords[1] - 40)], 3)
        pygame.draw.circle(screen, super_colour, (coords[0] + 50, coords[1] - 30), 23, 3)

    pygame.draw.polygon(screen, colour, [(coords[0] + 29, coords[1] - 40), (coords[0] + 29, coords[1] - 80),
                                         (coords[0] + 44, coords[1] - 40)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 34, coords[1] - 40), (coords[0] + 49, coords[1] - 80),
                                         (coords[0] + 64, coords[1] - 40)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 54, coords[1] - 40), (coords[0] + 69, coords[1] - 80),
                                         (coords[0] + 69, coords[1] - 40)])
    pygame.draw.circle(screen, colour, (coords[0] + 50, coords[1] - 30), 23)


def draw_rock(col, screen, num):
    if col['rocks'][num].x > 1000:
        return None
    if col['rocks'][num].colour == 'white':
        colour = (255, 255, 255)
    else:
        colour = (10, 10, 10)
    super_colour = (0, 0, 0)
    coords = get_pos(col['rocks'][num].x, col['rocks'][num].y)
    if col['rocks'][num].colour == 'white':
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 35, coords[1] - 10), (coords[0] + 45, coords[1] - 80),
                                                   (coords[0] + 55, coords[1] - 10)], 2)
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 35, coords[1] - 60), (coords[0] + 35, coords[1] - 70),
                                                   (coords[0] + 55, coords[1] - 70), (coords[0] + 55, coords[1] - 60)],
                            2)
        pygame.draw.rect(screen, super_colour, pygame.Rect(coords[0] + 30, coords[1] - 60, 30, 10), 2)

        pygame.draw.circle(screen, super_colour, (coords[0] + 45, coords[1] - 70), 15, 4)

    pygame.draw.polygon(screen, colour, [(coords[0] + 35, coords[1] - 10), (coords[0] + 45, coords[1] - 80),
                                         (coords[0] + 55, coords[1] - 10)])
    pygame.draw.polygon(screen, colour, [(coords[0] + 35, coords[1] - 60), (coords[0] + 35, coords[1] - 70),
                                         (coords[0] + 55, coords[1] - 70), (coords[0] + 55, coords[1] - 60)])
    pygame.draw.rect(screen, colour, pygame.Rect(coords[0] + 30, coords[1] - 60, 30, 10))

    pygame.draw.circle(screen, colour, (coords[0] + 45, coords[1] - 70), 15)


def draw_pawn(col, screen, num):
    if col['pawns'][num].x > 1000:
        return None
    if col['pawns'][num].colour == 'white':
        colour = (255, 255, 255)
    else:
        colour = (10, 10, 10)
    super_colour = (0, 0, 0)
    coords = get_pos(col['pawns'][num].x, col['pawns'][num].y)
    if col['pawns'][num].colour == 'white':
        pygame.draw.polygon(screen, super_colour, [(coords[0] + 35, coords[1] - 10), (coords[0] + 45, coords[1] - 80),
                                                   (coords[0] + 55, coords[1] - 10)], 2)
        pygame.draw.rect(screen, super_colour, pygame.Rect(coords[0] + 30, coords[1] - 10, 30, 10), 3)
        pygame.draw.circle(screen, super_colour, (coords[0] + 45, coords[1] - 70), 15, 4)

    pygame.draw.polygon(screen, colour, [(coords[0] + 35, coords[1] - 10), (coords[0] + 45, coords[1] - 80),
                                         (coords[0] + 55, coords[1] - 10)])
    pygame.draw.rect(screen, colour, pygame.Rect(coords[0] + 30, coords[1] - 10, 30, 10))
    pygame.draw.circle(screen, colour, (coords[0] + 45, coords[1] - 70), 15)


def draw_all(screen, white, black, x_sp=-1, y_sp=-1, todrawlist=([], [], [], [])):
    '''
    draws the actual situation on board
    :param screen:
    goes 4 white chesses:param white:
    goes 4 black chesses:param black:
    None:return:
    '''

    '''draw board itself'''
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (120, 70, 0), pygame.Rect(5, 5, 735, 735))
    pygame.draw.rect(screen, (245, 220, 190), pygame.Rect(10, 10, 730, 730))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(10 + 90 * i, 10 + 90 * j, 90, 90))
    if x_sp != -1 and y_sp != -1:
        coords_sp = get_pos(x_sp, y_sp)
        coords_sp = (coords_sp[0], coords_sp[1] - 90)
        pygame.draw.rect(screen, (10, 190, 20), pygame.Rect(coords_sp[0], coords_sp[1], 90, 90))
    if todrawlist[0] != []:
        for z in range(len(todrawlist[0])):
            todrawcoords = get_pos(todrawlist[0][z], todrawlist[1][z])
            todrawcoords = (todrawcoords[0], todrawcoords[1] - 90)
            pygame.draw.rect(screen, (10, 10, 200), pygame.Rect(todrawcoords[0], todrawcoords[1], 90, 90))
    if len(todrawlist) == 4 and todrawlist[2] != []:
        for z in range(len(todrawlist[2])):
            todrawcoords = get_pos(todrawlist[2][z], todrawlist[3][z])
            todrawcoords = (todrawcoords[0], todrawcoords[1] - 90)
            pygame.draw.rect(screen, (170, 10, 20), pygame.Rect(todrawcoords[0], todrawcoords[1], 90, 90))

    '''draw white'''
    draw_king(white, screen)
    draw_queen(white, screen)
    for i in range(len(white['rocks'])):
        draw_rock(white, screen, i)
    for i in range(len(white['pawns'])):
        draw_pawn(white, screen, i)
    for i in range(len(white['bishops'])):
        draw_bishop(white, screen, i)
    for i in range(len(white['knights'])):
        draw_knight(white, screen, i)
    '''draw black'''
    for i in range(len(black['rocks'])):
        draw_rock(black, screen, i)
    for i in range(len(black['pawns'])):
        draw_pawn(black, screen, i)
    for i in range(len(black['bishops'])):
        draw_bishop(black, screen, i)
    for i in range(len(black['knights'])):
        draw_knight(black, screen, i)
    draw_queen(black, screen)
    draw_king(black, screen)
    for i in range(9):
        pygame.draw.line(screen, (0, 0, 0), (10, i * 90 + 10), (720, i * 90 + 10), 2)
        pygame.draw.line(screen, (0, 0, 0), (10 + i * 90, 10), (10 + i * 90, 720), 2)


def mark_pos_king(screen, col1, col2):
    listtomovex = []
    listtomovey = []
    listtohitx = []
    listtohity = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == j == 0):
                tocheckx = col1['king'].x + i
                tochecky = chr(ord((col1['king'].y)) + j)
                if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                    f = True
                    if f and col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                        f = False
                    for count in range(len(col1['pawns'])):
                        if f and col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                            f = False
                    for count in range(len(col1['knights'])):
                        if f and col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                            f = False
                    for count in range(len(col1['rocks'])):
                        if f and col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                            f = False
                    for count in range(len(col1['bishops'])):
                        if f and col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                            f = False
                    if f and col2['king'].x == tocheckx and col2['king'].y == tochecky:
                        f = False
                        listtohitx.append(tocheckx)
                        listtohity.append(tochecky)
                    if f and col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                        f = False
                        listtohitx.append(tocheckx)
                        listtohity.append(tochecky)
                    for count in range(len(col2['pawns'])):
                        if f and col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                            f = False
                            listtohitx.append(tocheckx)
                            listtohity.append(tochecky)
                    for count in range(len(col2['knights'])):
                        if f and col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                            f = False
                            listtohitx.append(tocheckx)
                            listtohity.append(tochecky)
                    for count in range(len(col2['rocks'])):
                        if f and col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                            f = False
                            listtohitx.append(tocheckx)
                            listtohity.append(tochecky)
                    for count in range(len(col1['bishops'])):
                        if f and col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                            f = False
                            listtohitx.append(tocheckx)
                            listtohity.append(tochecky)
                    if f:
                        listtomovex.append(tocheckx)
                        listtomovey.append(tochecky)
    return (listtomovex, listtomovey, listtohitx, listtohity)


def mark_pos_queen(screen, col1, col2):
    listtomovex = []
    listtomovey = []
    listtohitx = []
    listtohity = []
    flag_not2hit = -9
    for i1 in range(-1, -8, -1):
        j = 0
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['queen'].x + i
            tochecky = chr(ord((col1['queen'].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(-1, -8, -1):
        i = 0
        j = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['queen'].x + i
            tochecky = chr(ord((col1['queen'].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(1, 8):
        j = 0
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['queen'].x + i
            tochecky = chr(ord((col1['queen'].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(1, 8):
        j = i1
        i = 0
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['queen'].x + i
            tochecky = chr(ord((col1['queen'].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(-1, -8, -1):
        j = i1
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['queen'].x + i
            tochecky = chr(ord((col1['queen'].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(1, 8):
        j = -i1
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['queen'].x + i
            tochecky = chr(ord((col1['queen'].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(-1, -8, -1):
        j = -i1
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['queen'].x + i
            tochecky = chr(ord((col1['queen'].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(1, 8):
        j = i1
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['queen'].x + i
            tochecky = chr(ord((col1['queen'].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    return (listtomovex, listtomovey, listtohitx, listtohity)


def mark_pos_rock(screen, col1, col2, num):
    listtomovex = []
    listtomovey = []
    listtohitx = []
    listtohity = []
    flag_not2hit = -9
    for i1 in range(-1, -8, -1):
        j = i1
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['rocks'][num].x + i
            tochecky = chr(ord((col1['rocks'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if num != count and col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovey.append(tochecky)
                    listtomovex.append(tocheckx)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(1, 8):
        j = -i1
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['rocks'][num].x + i
            tochecky = chr(ord((col1['rocks'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if num != count and col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(-1, -8, -1):
        j = -i1
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['rocks'][num].x + i
            tochecky = chr(ord((col1['rocks'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1

                if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if num != count and col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(1, 8):
        j = i1
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['rocks'][num].x + i
            tochecky = chr(ord((col1['rocks'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1

                if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if num != count and col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    return (listtomovex, listtomovey, listtohitx, listtohity)


def mark_pos_bishop(screen, col1, col2, num):
    listtomovex = []
    listtomovey = []
    listtohitx = []
    listtohity = []
    flag_not2hit = -9
    for i1 in range(-1, -8, -1):
        j = 0
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['bishops'][num].x + i
            tochecky = chr(ord((col1['bishops'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                    f = False
                    flag_not2hit = i1

                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if count != num and col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(-1, -8, -1):
        i = 0
        j = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['bishops'][num].x + i
            tochecky = chr(ord((col1['bishops'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1

                if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if count != num and col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(1, 8):
        j = 0
        i = i1
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['bishops'][num].x + i
            tochecky = chr(ord((col1['bishops'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if num != count and col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    for i1 in range(1, 8):
        j = i1
        i = 0
        enemy = False
        if flag_not2hit == -9:
            tocheckx = col1['bishops'][num].x + i
            tochecky = chr(ord((col1['bishops'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True
                cont2check = True
                if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                    f = False
                    flag_not2hit = i1
                for count in range(len(col1['pawns'])):
                    if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['knights'])):
                    if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['rocks'])):
                    if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if num != count and col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                        f = False
                        flag_not2hit = i1
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False

                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                    enemy = True
                    flag_not2hit = i1
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                        flag_not2hit = i1
                if f:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    flag_not2hit = -9
    return (listtomovex, listtomovey, listtohitx, listtohity)


def mark_pos_knight(screen, col1, col2, num):
    listtomovex = []
    listtomovey = []
    listtohitx = []
    listtohity = []
    need2checkx = [-2, -2, -1, -1, 1, 1, 2, 2]
    need2checky = [-1, 1, -2, 2, -2, 2, -1, 1]
    for k in range(len(need2checkx)):
        i = need2checkx[k]
        i1 = i
        enemy = False
        j = need2checky[k]
        tocheckx = col1['knights'][num].x + i
        tochecky = chr(ord((col1['knights'][num].y)) + j)
        if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
            f = True
            cont2check = True
            if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                f = False

            if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                f = False

            for count in range(len(col1['pawns'])):
                if col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                    f = False
            for count in range(len(col1['knights'])):
                if count != num and col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                    f = False
            for count in range(len(col1['rocks'])):
                if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                    f = False
            for count in range(len(col1['bishops'])):
                if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                    f = False
            if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                f = False

            if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                f = False
                enemy = True
            for count in range(len(col2['pawns'])):
                if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                    f = False
                    enemy = True
            for count in range(len(col2['knights'])):
                if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                    f = False
                    enemy = True
            for count in range(len(col2['rocks'])):
                if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                    f = False
                    enemy = True
            for count in range(len(col1['bishops'])):
                if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                    f = False
                    enemy = True
            if f:
                listtomovex.append(tocheckx)
                listtomovey.append(tochecky)
            if enemy:
                listtohitx.append(tocheckx)
                listtohity.append(tochecky)
    return (listtomovex, listtomovey, listtohitx, listtohity)


def mark_pos_pawn(screen, col1, col2, num):
    listtomovex = []
    listtomovey = []
    listtohitx = []
    listtohity = []
    sup = False
    if col1['pawns'][num] == 'white':
        need2checkx = [0]
        need2checky = [1]
        if col1['pawns'][num].moved == 0:
            need2checkx.append(0)
            need2checky.append(2)
    else:
        need2checkx = [0]
        need2checky = [1]
        if col1['pawns'][num].moved == 0:
            need2checkx.append(0)
            need2checky.append(2)
    for k in range(len(need2checkx)):
        i = need2checkx[k]
        i1 = i
        enemy = False
        j = need2checky[k]
        tocheckx = col1['pawns'][num].x + i
        tochecky = chr(ord((col1['pawns'][num].y)) + j)
        if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
            f = True
            cont2check = True
            if col1['king'].x == tocheckx and col1['king'].y == tochecky:
                f = False
            if col1['queen'].x == tocheckx and col1['queen'].y == tochecky:
                f = False
            for count in range(len(col1['pawns'])):
                if count != num and col1['pawns'][count].x == tocheckx and col1['pawns'][count].y == tochecky:
                    f = False
            for count in range(len(col1['knights'])):
                if col1['knights'][count].x == tocheckx and col1['knights'][count].y == tochecky:
                    f = False
            for count in range(len(col1['rocks'])):
                if col1['rocks'][count].x == tocheckx and col1['rocks'][count].y == tochecky:
                    f = False
            for count in range(len(col1['bishops'])):
                if col1['bishops'][count].x == tocheckx and col1['bishops'][count].y == tochecky:
                    f = False
                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    f = False
                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    f = False
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        f = False
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        f = False
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        f = False
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False

            if k % 2 == 0:
                sup = False
            if f:
                if not sup:
                    listtomovex.append(tocheckx)
                    listtomovey.append(tochecky)
            else:
                sup = True
    if col1['pawns'][num] == 'white':
        need2checkx = [1, -1]
        need2checky = [1, 1]
    else:
        need2checkx = [1, -1]
        need2checky = [-1, -1]
    if True:
        for k in range(len(need2checkx)):
            i = need2checkx[k]
            i1 = i
            enemy = False
            j = need2checky[k]
            tocheckx = col1['pawns'][num].x + i
            tochecky = chr(ord((col1['pawns'][num].y)) + j)
            if 1 <= tocheckx <= 8 and 'A' <= tochecky <= 'H':
                f = True

                if col2['king'].x == tocheckx and col2['king'].y == tochecky:
                    enemy = True
                if col2['queen'].x == tocheckx and col2['queen'].y == tochecky:
                    enemy = True
                for count in range(len(col2['pawns'])):
                    if col2['pawns'][count].x == tocheckx and col2['pawns'][count].y == tochecky:
                        enemy = True
                for count in range(len(col2['knights'])):
                    if col2['knights'][count].x == tocheckx and col2['knights'][count].y == tochecky:
                        enemy = True
                for count in range(len(col2['rocks'])):
                    if col2['rocks'][count].x == tocheckx and col2['rocks'][count].y == tochecky:
                        enemy = True
                for count in range(len(col1['bishops'])):
                    if col2['bishops'][count].x == tocheckx and col2['bishops'][count].y == tochecky:
                        f = False
                        enemy = True
                if enemy:
                    listtohitx.append(tocheckx)
                    listtohity.append(tochecky)
    return (listtomovex, listtomovey, listtohitx, listtohity)


def check_if_anything(screen, col, x, y):
    s = '###'
    if col['king'].x == x and col['king'].y == y:
        s = 'king'
        return [s, '-1']
    if col['queen'].y == y and col['queen'].x == x:
        s = 'queen'
        return [s, '-1']
    for i in range(len(col['pawns'])):
        if col['pawns'][i].x == x and col['pawns'][i].y == y:
            s = 'pawns'
            return [s, str(i)]
    for i in range(len(col['knights'])):
        if col['knights'][i].x == x and col['knights'][i].y == y:
            s = 'knights'
            return [s, str(i)]
    for i in range(len(col['bishops'])):
        if col['bishops'][i].x == x and col['bishops'][i].y == y:
            s = 'bishops'
            return [s, str(i)]
    for i in range(len(col['rocks'])):
        if col['rocks'][i].x == x and col['rocks'][i].y == y:
            s = 'rocks'
            return [s, str(i)]
    return [s, str(-2)]


def main():
    '''
    todrawlist shows list of spaces that are possible 4 moves and attack of the pointed/selected figure

    None to be returned
    '''
    pygame.init()
    width = 1500
    height = 1000
    todrawlist = ([], [], [], [])
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('chess1.0')
    clock = pygame.time.Clock()
    '''
    init white figures on the board
    '''
    white = {}
    white['king'] = King('white')
    white['queen'] = Queen('white')
    pawns = []
    for i in range(8):
        pawns.append(Pawn('white', i))
    white['pawns'] = pawns[:]
    rocks = [Rock('white', 0), Rock('white', 1)]
    white['rocks'] = rocks[:]
    knights = [Knight('white', 0), Knight('white', 1)]
    white['knights'] = knights[:]
    bishpos = [Bishop('white', 0), Bishop('white', 1)]
    white['bishops'] = bishpos[:]
    '''
    init black figures at the board
    '''
    black = {}
    black['king'] = King('black')
    black['queen'] = Queen('black')
    pawns = []
    take = False
    for i in range(8):
        pawns.append(Pawn('black', i))
    black['pawns'] = pawns[:]
    rocks = [Rock('black', 0), Rock('black', 1)]
    black['rocks'] = rocks[:]
    knights = [Knight('black', 0), Knight('black', 1)]
    black['knights'] = knights[:]
    bishpos = [Bishop('black', 0), Bishop('black', 1)]
    black['bishops'] = bishpos[:]
    k = Move()
    pawntocheck=Pawn('green',100)
    while True:
        dt = clock.tick(100) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN
                     and event.key == pygame.K_ESCAPE):
                sys.exit()
        coords = pygame.mouse.get_pos()
        # coords inted tuple of coords
        coords = (int(coords[0]), int(coords[1]))
        if 10 <= coords[0] <= 730 and 10 <= coords[1] <= 730:
            coords = ((coords[0] - 10) // 90, (coords[1] - 10) // 90)
            mousex = 1 + coords[0]
            mousey = chr(((7 - coords[1]) + ord('A')))
            check = check_if_anything(screen, white, mousex, mousey) if k.whose_move == 'white' else \
                check_if_anything(screen, black, mousex, mousey)
            # check is list of 2 elems in case there is any piece in this spot and '###' of none


            if pygame.key.get_pressed()[pygame.K_a] and not take and check[0]!='###':

                take=True
                todrawlist = [[], [], [], []]
                if check[0] == 'king':
                    todrawlist = mark_pos_king(screen, white, black) if k.whose_move == 'white' else \
                        mark_pos_king(screen, black, white)
                    hold_figure=white['king'] if k.whose_move=='white' else \
                                black['king']
                elif check[0] == 'queen':
                    todrawlist = mark_pos_queen(screen, white, black) if k.whose_move == 'white' else \
                        mark_pos_queen(screen, black, white)
                    hold_figure = white['queen'] if k.whose_move == 'white' else \
                        black['queen']
                elif check[0] == 'rocks':
                    todrawlist = mark_pos_rock(screen, white, black, int(check[1])) if k.whose_move == 'white' else \
                        mark_pos_rock(screen, black, white, int(check[1]))
                    hold_figure = white['rocks'][int(check[1])] if k.whose_move == 'white' else \
                        black['rocks'][int(check[1])]
                elif check[0] == 'bishops':
                    todrawlist = mark_pos_bishop(screen, white, black, int(check[1])) if k.whose_move == 'white' else \
                        mark_pos_bishop(screen, black, white, int(check[1]))
                    hold_figure = white['bishops'][int(check[1])] if k.whose_move == 'white' else \
                        black['bishops'][int(check[1])]
                elif check[0] == 'knights':
                    todrawlist = mark_pos_knight(screen, white, black, int(check[1])) if k.whose_move == 'white' else \
                        mark_pos_knight(screen, black, white, int(check[1]))
                    hold_figure = white['knights'][int(check[1])] if k.whose_move == 'white' else \
                        black['knights'][int(check[1])]
                elif check[0] == 'pawns':

                    todrawlist = mark_pos_pawn(screen, white, black, int(check[1])) if k.whose_move == 'white' else \
                        mark_pos_pawn(screen, black, white, int(check[1]))
                    hold_figure = white['pawns'][int(check[1])] if k.whose_move == 'white' else \
                        black['pawns'][int(check[1])]
            elif pygame.key.get_pressed()[pygame.K_d] and take:
                movedone=False
                for specialcount in range(len(todrawlist[0])):
                    if todrawlist[0][specialcount]==mousex and todrawlist[1][specialcount]==mousey:
                        take=False
                        hold_figure.fixwith(mousex,mousey)
                        if type(hold_figure)==type(pawntocheck):
                            hold_figure.moved=0
                        movedone=True
                        break
                for specialcount in range(len(todrawlist[2])):
                    if todrawlist[2][specialcount]==mousex and todrawlist[3][specialcount]==mousey:
                        take=False
                        hold_figure.fixwith(mousex,mousey)
                        zetta=white if k.whose_move=='black' else black
                        if zetta['queen'].x==mousex and zetta['queen'].y==mousey:
                            zetta['queen'].x=-100
                            zetta['queen'].y='P'
                            movedone=True
                        for noidea in range(len(zetta['pawns'])):
                                if zetta['pawns'][noidea].x==mousex and zetta['pawns'][noidea]==mousey:
                                    zetta['pawns'].pop(noidea)
                                    movedone=True
                                    break
                        for noidea in range(len(zetta['knights'])):
                                if zetta['knights'][noidea].x == mousex and zetta['knights'][noidea] == mousey:
                                    zetta['knights'].pop(noidea)
                                    movedone=True
                                    break
                        for noidea in range(len(zetta['bishops'])):
                                if zetta['bishops'][noidea].x == mousex and zetta['bishops'][noidea] == mousey:
                                    zetta['bishops'].pop(noidea)
                                    movedone=True
                                    break
                        for noidea in range(len(zetta['rocks'])):
                                if zetta['rocks'][noidea].x == mousex and zetta['rocks'][noidea] == mousey:
                                    zetta['rocks'].pop(noidea)
                                    movedone=True
                                    break
                if movedone:
                    print(100)
                    change_move(k)
                    print(k.whose_move)
            #after here i mean
            if not take:
                todrawlist = [[], [], [], []]
                if check[0] == 'king':
                    todrawlist = mark_pos_king(screen, white, black) if k.whose_move == 'white' else \
                        mark_pos_king(screen, black, white)
                elif check[0] == 'queen':
                    todrawlist = mark_pos_queen(screen, white, black) if k.whose_move == 'white' else \
                        mark_pos_queen(screen, black, white)
                elif check[0] == 'rocks':
                    todrawlist = mark_pos_rock(screen, white, black, int(check[1])) if k.whose_move == 'white' else \
                        mark_pos_rock(screen, black, white, int(check[1]))
                elif check[0] == 'bishops':
                    todrawlist = mark_pos_bishop(screen, white, black, int(check[1])) if k.whose_move == 'white' else \
                        mark_pos_bishop(screen, black, white, int(check[1]))
                elif check[0] == 'knights':
                    todrawlist = mark_pos_knight(screen, white, black, int(check[1])) if k.whose_move == 'white' else \
                        mark_pos_knight(screen, black, white, int(check[1]))
                elif check[0] == 'pawns':
                    todrawlist = mark_pos_pawn(screen, white, black, int(check[1])) if k.whose_move == 'white' else \
                        mark_pos_pawn(screen, black, white, int(check[1]))
            #after this block everything is known about spots 2 go and hit 2

            draw_all(screen, white, black, mousex, mousey, todrawlist)
        else:
            draw_all(screen, white, black)
        pygame.display.flip()


main()
