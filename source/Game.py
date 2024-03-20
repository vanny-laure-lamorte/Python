import pygame
import time

from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen
from source.Board import Board 
import random

class Game(Element, Screen): 
    def __init__(self, size, username):
        self.board = Board(size)
        Element.__init__(self)
        Screen.__init__(self)
        self.size = size
        self.board_list = []
        self.game_running = True
        self.discovered_tile = []
        self.bomb_count = self.board.is_bomb()
        self.username = username
        self.tile_count = str(self.size[0]*self.size[1])

          # Timer
        self.start_time = time.time()
        self.clock = pygame.time.Clock()

        # Chargement des images
        self.img_game_chrono = pygame.image.load('assets/image/game_chrono.png').convert_alpha()
        self.img_tom = pygame.image.load('assets/image/game_tom.png').convert_alpha()
        self.img_game_flag = pygame.image.load('assets/image/game_flag.png').convert_alpha()
        self.img_tile_empty = pygame.image.load('assets/image/sprite/Tile_empty.png').convert_alpha()
        self.img_tile_not_revealed = pygame.image.load('assets/image/sprite/Tile_not_revealed.png').convert_alpha()
        self.img_tile_bomb = pygame.image.load('assets/image/sprite/Tile_is_bomb.png').convert_alpha()
        self.img_picture_restart = pygame.image.load('assets/image/game_restart.png').convert_alpha()
        self.img_picture_win = pygame.image.load('assets/image/game_win.png').convert_alpha()
        self.img_picture_lose = pygame.image.load('assets/image/game_mad.png').convert_alpha()

    def timer_game(self):

        self.elapsed_time = time.time() - self.start_time

        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        self.formatted_time = "{:02d}:{:02d}".format(minutes, seconds)

          # Timer
        self.start_time = time.time()
        self.clock = pygame.time.Clock()

    def timer_game(self):

        self.elapsed_time = time.time() - self.start_time

        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        self.formatted_time = "{:02d}:{:02d}".format(minutes, seconds)

    def design(self):
        # Background
        self.screen_color(self.orange)

        # Title

        self.text_not_align(self.font1, 50,"Mines Weeper ", self.white, 320, 280)

        # Timer        
        self. rect_full(self.white, 890, 160, 80, 90, 5)
        self.rect_border(self.orange1, 890, 160, 80, 90, 3, 5)

        self.image_not_center("game_chrono", 855, 115, 70, 70, self.img_game_chrono)
        self.text_not_align(self.font3, 15, self.formatted_time, self.black, 875, 185)


        # self.image_not_center("game_chrono", 855, 115, 70, 70, self.img_game_chrono)
        # self.text_not_align(self.font3, 15, "777", self.black, 880, 185)


        # Tom

        self. rect_full(self.white, 890, 260, 80, 90, 5)
        self.rect_border(self.orange1, 890, 260, 80, 90, 3, 5)
        self.image_not_center("tom", 855, 215, 70, 70, self.img_tom)
        self.text_not_align(self.font3, 12, "X", self.black, 865, 285)
        self.text_not_align(self.font3, 15, self.bomb_count, self.black, 880, 283)

        # self. rect_full(self.white, 890, 260, 80, 90, 5)
        # self.rect_border(self.orange1, 890, 260, 80, 90, 3, 5)
        # self.image_not_center("tom", 785, 130, 70, 70, self.img_tom)
        # self.text_not_align(self.font3, 12, "X", self.black, 860, 170)
        # self.text_not_align(self.font3, 15, self.bomb_count, self.black, 870, 168)

        # Red flag

        self. rect_full(self.white, 890, 360, 80, 90, 5)
        self.rect_border(self.orange1, 890, 360, 80, 90, 3, 5)
        self.image_not_center("game_flag", 860, 320, 55, 55, self.img_game_flag)
        self.text_not_align(self.font3, 12, "X", self.black, 865, 385)
        self.text_not_align(self.font3, 15, "77", self.black, 880, 383)
     
        # Red tiles
        self. rect_full(self.white, 890, 460, 80, 90, 5)
        self.rect_border(self.orange1, 890, 460, 80, 90, 3, 5)
        self.image_not_center("tile", 868, 425, 40, 40, self.img_tile_not_revealed)
        self.text_not_align(self.font3, 12, "X", self.black, 865, 485)
        self.text_not_align(self.font3, 15,self.tile_count, self.black, 880, 483)

        # Rect Jerry
        self.button_hover(62, 310, 110, 200, self.orange, self.white, self.red1, self.white, "", self.font1, self.white, 12, 2, 5)

        # Retour Menu
        self.rect_menu = self.button_hover(890, 30, 100, 40, self.orange1, self.white, self.yellow, self.white, "BACK TO MENU", self.font2, self.white,18, 2, 5)
        
        # Player info
        self.text_not_align(self.font3, 100, self.username , self.pink, 360, 10)

    def game_restart(self):
        self.image_not_center("picture restart", 10, 220, 100, 170, self.img_picture_restart)

    def game_win(self): 
        self.image_not_center("picture win", 10, 200, 100, 200, self.img_picture_win)

    def game_lose(self): 
        self.image_not_center("picture lose", 15, 220, 100, 180, self.img_picture_lose)

    def draw_board(self):
        self.board_list = []
        for row in range(self.size[1]):
            for col in range(self.size[0]):
                x = col * 51
                y = row * 51
                if (row, col) not in [item[0] for item in self.discovered_tile]:
                    tile_rect = pygame.Rect(self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50)
                    self.board_list.append((tile_rect, (row, col)))
                    self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_not_revealed)

                else: 
                    discovered = False
                    for tile in self.discovered_tile:
                        if tile[0] == (row, col):
                            discovered = tile[1]
                            break
                    if discovered:
                        self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_bomb)

                    else:
                        self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_empty)


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

                    if self.rect_menu.collidepoint(event.pos):
                        self.game_running = False
                    elif event.button == 1:
                        for tile_rect, (row, col) in self.board_list:
                            if tile_rect.collidepoint(event.pos):
                                self.check_bomb(row, col)
                    elif event.button == 3:
                        pass 

                        
            self.timer_game()
            self.design()
            self.draw_board()
            # self.game_restart()
            self.game_win()
            # self.game_lose()
            self.update()