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
        self.image_not_center("game_chrono", 780, 50, 80, 80, "game_chrono")
        self.text_not_align(self.font3, 15 ,self.formatted_time, self.black, 852, 90)

        # Tom
        self.image_not_center("tom", 785, 130, 75, 75, "game_tom")
        self.text_not_align(self.font3, 12,"X", self.black, 860, 170)
        self.text_not_align(self.font3, 15,"24", self.black, 870, 168)

        # Red flag
        self.image_not_center("game_flag", 785, 200, 60, 60, "game_flag")
        self.text_not_align(self.font3, 12,"X", self.black, 860, 240)
        self.text_not_align(self.font3, 15,"24", self.black, 870, 238)

      
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
                        
            self.timer_game()
            self.design()
            self.draw_board()
            self.update()
