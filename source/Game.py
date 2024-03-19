import pygame
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

    def design(self):
        # Background
        self.screen_color((220, 130, 77))

    def draw_board(self):
        self.size = (12, 12)
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
                        
            self.design()
            self.draw_board()
            self.update()
