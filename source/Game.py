import pygame
import time

from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen
from source.Board import Board 
import random

FLAG = 1
QUESTION_MARK = 2
EMPTY = 0

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
        self.img_tile_flagged = pygame.image.load('assets/image/sprite/Tile_flagged.png').convert_alpha()
        self.img_tile_question_mark = pygame.image.load('assets/image/sprite/Tile_question_mark.png').convert_alpha()

        self.current_flag_state = EMPTY
        self.flag_tile = None

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

        # Timer
        self.image_not_center("game_chrono", 780, 50, 70, 70, self.img_game_chrono)
        self.text_not_align(self.font3, 15, self.formatted_time, self.black, 852, 90)

        # Tom
        self.image_not_center("tom", 785, 130, 70, 70, self.img_tom)
        self.text_not_align(self.font3, 12, "X", self.black, 860, 170)
        self.text_not_align(self.font3, 15, "24", self.black, 870, 168)

        # Red flag
        self.image_not_center("game_flag", 785, 220, 80, 80, self.img_game_flag)
        self.text_not_align(self.font3, 12, "X", self.black, 860, 250)
        self.text_not_align(self.font3, 15, "24", self.black, 870, 248)

        # Red tiles
        self.image_not_center("tile", 800, 310, 40, 40, self.img_tile_not_revealed)
        self.text_not_align(self.font3, 12, "X", self.black, 860, 330)
        self.text_not_align(self.font3, 15, "777", self.black, 870, 328)

        # Rect Jerry
        self.button_hover(62, 310, 110, 200, self.orange, self.white, self.red1, self.white, "", self.font1, self.white, 12, 2, 5)

        # Retour Menu
        self.rect_menu = self.button_hover(62, 45, 100, 40, self.red1, self.white, self.yellow, self.white, "BACK TO MENU", self.font2, self.white,18, 2, 5)

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

                    if self.flag_tile == (row, col):
                        if self.current_flag_state == FLAG:
                            self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_flagged)
                        elif self.current_flag_state == QUESTION_MARK:
                            self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_question_mark)

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
                    if event.button == 1:
                        for tile_rect, (row, col) in self.board_list:
                            if tile_rect.collidepoint(event.pos):
                                self.check_bomb(row, col)
                    elif event.button == 3:
                        for tile_rect, (row, col) in self.board_list:
                            if tile_rect.collidepoint(event.pos) and (row, col) not in [item[0] for item in self.discovered_tile]:
                                if self.current_flag_state == EMPTY:
                                    self.current_flag_state = FLAG
                                elif self.current_flag_state == FLAG:
                                    self.current_flag_state = QUESTION_MARK
                                else:
                                    self.current_flag_state = EMPTY

                                self.flag_tile = (row, col)
                                break
                    elif self.rect_menu.collidepoint(event.pos):
                            self.game_running = False

            self.timer_game()
            self.design()
            self.draw_board()
            # self.game_restart()
            self.game_win()
            # self.game_lose()
            self.update()