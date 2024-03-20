import pygame
from os import walk
from source.Board import set_up

row_num = 9
col_num = 29
tile_size = 40
bomb_num = 50

game_over = False
game_clear = False

FPS = 60
clock = pygame.time.Clock()

field = set_up()

images = {}
path = "assets/img/sprite"
for _, __, img_files in walk(path):
    for image in img_files:
        full_path = path + "/" + image
        img = pygame.image.load(full_path)
        img = pygame.transform.scale(img, (tile_size, tile_size))
        images[image.split(".")[0]] = img

print(field)