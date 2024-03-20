import random
from source.settings import *
from source.tile import Tile

def set_up():

    field = []
    for row in range(row_num):
        tile_list = []
        for col in range(col_num):
            tile = Tile((col * tile_size, row * tile_size), images["Tile_empty"])
            tile_list.append(tile)
        field.append(tile_list)

    count = 0
    while count < bomb_num:
        x = random.randint(0, col_num - 1)
        y = random.randint(0, row_num - 1)
        tile = field[y][x]
        if tile.bomb == False:
            tile.bomb = True
            tile.neighbor_bomb_num = -1
            count += 1

    for row_index, tile_list in enumerate(field):
        for col_index, tile in enumerate(tile_list):
            if tile.bomb:
                for y_offset in range(-1, 2):
                    for x_offset in range(-1, 2):
                        x_pos = col_index + x_offset
                        y_pos = row_index + y_offset
                        if 0 <= x_pos < col_num and 0 <= y_pos < row_num and field[y_pos][x_pos].bomb == False:
                            field[y_pos][x_pos].neighbor_bomb_num += 1
    return field

def open_tile(x, y, field):

    if field[y][x].check:
        return

    field[y][x].check = True
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            col = x + x_offset
            row = y + y_offset
            if 0 <= col < col_num and 0 <= row < row_num and field[row][col].image != images["Tile_flagged"]:
                field[row][col].open = True
                if field[row][col].neighbor_bomb_num == 0:
                    open_tile(col, row, field)