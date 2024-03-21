import pygame, time

from source.pygame_manager.Element import Element
from source.Board import Board 

class Game(Element): 
    def __init__(self, size, username):
        self.board = Board(size)
        Element.__init__(self)

        # Bomb
        self.size = size
        self.board_list = []
        self.game_running = True
        self.discovered_tile = []
        self.bomb_count = self.board.is_bomb()
        self.username = username
        self.tile_count = int(self.size[0]*self.size[1])
        
        # Timer
        self.timer_started = False
        self.formatted_time = "00:00"       

        # Loading pictures
        self.img_game_chrono = pygame.image.load('assets/image/game_chrono.png').convert_alpha()
        self.img_tom = pygame.image.load('assets/image/game_tom.png').convert_alpha()
        # self.img_game_flag = pygame.image.load('assets/image/game_flag.png').convert_alpha()
        self.img_tile_empty = pygame.image.load('assets/image/sprite/Tile_empty.png').convert_alpha()
        self.img_tile_not_revealed = pygame.image.load('assets/image/sprite/Tile_not_revealed.png').convert_alpha()
        self.img_tile_bomb = pygame.image.load('assets/image/sprite/Tile_is_bomb.png').convert_alpha()
        self.img_picture_restart = pygame.image.load('assets/image/game_restart.png').convert_alpha()
        self.img_picture_win = pygame.image.load('assets/image/game_win.png').convert_alpha()
        self.img_picture_lose = pygame.image.load('assets/image/game_lose.png').convert_alpha()
        self.img_picture_flag = pygame.image.load('assets/image/game_f.png').convert_alpha()
        self.img_picture_question = pygame.image.load('assets/image/game_q.png').convert_alpha()
        self.img_best = pygame.image.load('assets/image/game_best.png').convert_alpha()
        self.img_jerry = pygame.image.load('assets/image/icon-jerry1.png').convert_alpha()
        self.img_game_flag= pygame.image.load('assets/image/game_f.png').convert_alpha()


    def timer_game(self):
        self.elapsed_time = time.time() - self.start_time
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        self.formatted_time = "{:02d}:{:02d}".format(minutes, seconds)

    def design(self):
        # Background
        self.screen_color(self.orange)

        # Title
        self.text_not_align(self.font1, 30,"Mines Weeper ", self.white, 8, 10)
        self.text_not_align(self.font1, 18,"— by L M, H N & VL", self.white, 10, 38)

        # Logo Jerry
        self.image_not_center("picture win", 855, 25, 80, 80, self.img_jerry)

        # Display player name
        self.text_center(self.font2, 30, f"DONT GET CAUGHT BY THE CAT {self.username} !", self.white, 460, 30)

        # Retour Menu
        self.rect_menu = self.button_hover(75, 320, 130, 40, self.orange1, self.white, self.orange1, self.white, "BACK TO MENU", self.font2, self.white,25, 2, 5)

        # Restart
        self.button_hover(75, 370, 130, 40, self.orange1, self.white, self.orange1, self.white, "RESTART", self.font2, self.white, 25, 2, 5)

        # Best time
        self.rect_full(self.orange1, 75, 505, 130, 200, 5)
        self.rect_border(self.white, 75, 505, 130, 200, 3, 5)
        self.text_not_align(self.font2, 25,"Best", self.white, 65, 450)
        self.text_not_align(self.font2, 25," Player Time ", self.white, 25, 475)
        self.image_not_center("Winner", 20, 430, 40, 40, self.img_best)

        self.text_not_align(self.font2, 40,"02:14", self.white, 45, 525)
        self.text_not_align(self.font2, 20,"by Lucy Madec", self.white, 25, 560)

        # Timer        
        self. rect_full(self.white, 890, 160, 80, 90, 5)
        self.rect_border(self.orange1, 890, 160, 80, 90, 3, 5)
        self.image_not_center("game_chrono", 855, 115, 70, 70, self.img_game_chrono)
        self.text_not_align(self.font3, 15, self.formatted_time, self.black, 875, 185)

        # Tom
        self. rect_full(self.white, 890, 260, 80, 90, 5)
        self.rect_border(self.orange1, 890, 260, 80, 90, 3, 5)
        self.image_not_center("tom", 855, 215, 70, 70, self.img_tom)
        self.text_not_align(self.font3, 12, "X", self.black, 865, 285)
        self.text_not_align(self.font3, 15, self.bomb_count, self.black, 880, 283)

        # Red flag
        self. rect_full(self.white, 890, 360, 80, 90, 5)
        self.rect_border(self.orange1, 890, 360, 80, 90, 3, 5)
        self.image_not_center("game_flag", 860, 320, 55, 55, self.img_game_flag)
        self.text_not_align(self.font3, 12, "X", self.black, 865, 385)
        self.text_not_align(self.font3, 15, "77", self.black, 880, 383)
     
        # Red tiles
        remaining_tiles = self.tile_count - len(self.discovered_tile)
        print( self.discovered_tile)
        self. rect_full(self.white, 890, 460, 80, 90, 5)
        self.rect_border(self.orange1, 890, 460, 80, 90, 3, 5)
        self.image_not_center("tile", 868, 425, 40, 40, self.img_tile_not_revealed)
        self.text_not_align(self.font3, 12, "X", self.black, 865, 485)
        self.text_not_align(self.font3, 15, str(remaining_tiles), self.black, 880, 483)

    # Display win message
    def game_win(self): 
        self.text_not_align(self.font2, 20, "You Just Won", self.green, 15, 225)
        self.text_not_align(self.font2, 20, "The Cheese ! ", self.green, 15, 250)
        self.image_not_center("picture win", 10, 120, 100, 100, self.img_picture_win)

    # Display lose message
    def game_lose(self): 
        self.text_not_align(self.font2, 20, "You Lose...", self.red, 15, 225)
        self.text_not_align(self.font2, 20, "No Cheese Caught ", self.red, 15, 250)
        self.image_not_center("picture loose", 10, 120, 100, 100, self.img_picture_lose)

    def draw_board(self):

        # Display grid
        for row in range(self.size[1]):
            for col in range(self.size[0]):
                x = col * 51
                y = row * 51

                # Display tile not discovered
                if (row, col) not in [item[0] for item in self.discovered_tile]:
                    tile_rect = pygame.Rect(self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50)
                    self.board_list.append((tile_rect, (row, col), 0))
                    self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_not_revealed)

                # Display empty tile or bomb
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

    # Check if tile is a bomb
    def check_bomb(self, row, col):
        if self.board.is_bomb_at(row, col):
            if (row, col) not in [item[0] for item in self.discovered_tile]:
                print("Bombe trouvée à la position", (row, col))
                self.discovered_tile.append(((row, col), True))
        else:
            if (row, col) not in [item[0] for item in self.discovered_tile]:
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

                    elif event.button == 1:  # Left click

                        for tile_rect, (row, col), z in self.board_list:
                            if tile_rect.collidepoint(event.pos):
                                self.check_bomb(row, col)
                                if not self.timer_started:
                                    self.timer_started = True
                                    self.start_time = time.time()


                    elif event.button == 3: # Right click - Flag, question, empty tile
                        for item in self.board_list:
                            if item[0].collidepoint(event.pos):

                                if item[2] == 0:  
                                    item[2] = 1  
                                elif item[2] == 1:  
                                    item[2] = 2
                                else:
                                    item[2]= 0
                        self.draw_board()

                    elif self.rect_menu.collidepoint(event.pos):
                            self.game_running = False

                    
            # Start Timer
            if self.timer_started:
                self.timer_game()

            self.design()
            self.draw_board()
            self.game_lose()
            self.update()