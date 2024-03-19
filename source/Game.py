import pygame
import time

from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen
from source.Board import Board 

class Game (Element, Screen): 
    def __init__(self,size):
        self.board = Board(size)
        Element.__init__(self)
        Screen.__init__(self)
        self.x, self.y = 0,0
        self.game_running = True

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
        self.screen_color((220, 130, 77))

        # Timer
        self.image_not_center("game_chrono", 780, 50, 70, 70, "game_chrono")
        self.text_not_align(self.font3, 15 ,self.formatted_time, self.black, 852, 90)

        # Tom
        self.image_not_center("tom", 785, 130, 70, 70, "game_tom")
        self.text_not_align(self.font3, 12,"X", self.black, 860, 170)
        self.text_not_align(self.font3, 15,"24", self.black, 870, 168)

        # Red flag
        self.image_not_center("game_flag", 785, 220, 80, 80, "game_flag")
        self.text_not_align(self.font3, 12,"X", self.black, 860, 250)
        self.text_not_align(self.font3, 15,"24", self.black, 870, 248)

        # Red tiles
        self.image_not_center("tile", 800, 310, 40, 40, "sprite/Tile_not_revealed")
        self.text_not_align(self.font3, 12,"X", self.black, 860, 330)
        self.text_not_align(self.font3, 15,"777", self.black, 870, 328)

        # Rect Jerry
        self.button_hover(62, 310, 110, 200, self.orange, self.white, self.red1, self.white, "", self.font1, self.white, 12, 2, 5)

        # Retour Menu
        self.rect_menu = self.button_hover(62, 45, 100, 40, self.red1, self.white, self.yellow, self.white, "BACK TO MENU", self.font2, self.white,18, 2, 5)



    def game_restart(self):
        self.image_not_center("picture restart", 10, 220, 100, 170, "game_restart")

    def game_win(self): 
        self.image_not_center("picture win", 10, 200, 100, 200, "game_win")

    def game_lose(self): 
        self.image_not_center("picture lose", 15, 220, 100, 180,"game_mad")


      
    def draw_board(self):
        self.size = (13, 13)
        self.board_list = []

        for row in range(self.size[0]):
            for col in range(self.size[1]):
                x = col * 51
                y = row * 51
                tile = self.image_not_center("tile", self.W//2-((self.size[0]*50//2)) + x, self.H//2-((self.size[1]*50//2)) + y, 50, 50, "sprite/Tile_not_revealed")
                self.board_list.append(tile)

    def game_run(self):

        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for tile in self.board_list:
                        if tile.collidepoint(event.pos):
                            if event.button == 1:
                                print(tile, "case")
                            elif event.button == 3:
                                print(tile, "flag")

                        elif self.rect_menu.collidepoint(event.pos):
                            self.game_running = False
                        
            self.timer_game()
            self.design()
            self.draw_board()
            # self.game_restart()
            self.game_win()
            # self.game_lose()
            self.update()
