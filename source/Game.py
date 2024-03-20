import pygame
from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen
from source.Board_test import Board 
import random

class Game(Element, Screen): 
    def __init__(self, size):
        self.board = Board(size)
        Element.__init__(self)
        Screen.__init__(self)
        self.size = size
        self.board_list = []
        self.game_running = True
        self.discovered_tile = []
        self.bomb_count = self.board.is_bomb()

    def design(self):
        # Background
        self.screen_color(self.orange)

    def draw_board(self):
        self.board_list = []
        for row in range(self.size[1]):
            for col in range(self.size[0]):
                x = col * 51
                y = row * 51
                if (row, col) not in [item[0] for item in self.discovered_tile]:
                    tile_rect = pygame.Rect(self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50)
                    self.board_list.append((tile_rect, (row, col)))
                    self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, "sprite/Tile_not_revealed")
                else: 
                    discovered = False
                    for tile in self.discovered_tile:
                        if tile[0] == (row, col):
                            discovered = tile[1]
                            break
                    if discovered:
                        self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, "sprite/Tile_is_bomb")
                    else:
                        self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, "sprite/Tile_empty")


    def check_bomb(self, row, col):
        if self.board.is_bomb_at(row, col):
            print("Bombe trouvée à la position", (row, col))
            self.discovered_tile.append(((row, col), True))
        else:
            print("Pas de bombe à la position", (row, col))
            self.discovered_tile.append(((row, col), False))

    def game_run(self):
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for tile_rect, (row, col) in self.board_list:
                            if tile_rect.collidepoint(event.pos):
                                self.check_bomb(row, col)
                    elif event.button == 3:
                        pass 
            print(self.bomb_count)
                        
            self.design()
            self.draw_board()
            self.update()
