import pygame, time, json

from source.pygame_manager.Element import Element
from source.Board import Board

FLAG = 1
QUESTION_MARK = 2
EMPTY = 0

class Game(Element):
    def __init__(self, size, username):
        self.board = Board(size)
        Element.__init__(self)

        # Bomb
        self.size = size
        self.board_list = []
        self.game_running = True
        self.game_finished = False
        self.flag_count = 0
        self.bomb_count = self.board.is_bomb()
        self.username = username
        self.tile_count = 0
        self.discovered_tile = []
        self.tile_states = {}
        self.current_flag_state = EMPTY
        self.flag_tile = None
        self.selected_tile = None
        self.bomb_count_final = 0
        self.timer = True
        self.best_time = float('inf')
        self.player_name = None

        # Timer
        self.timer_started = False
        self.formatted_time = "00:00"

        # Bomb 
        self.tile_is_bomb = False     
        self.bomb_count_final = 0

        # Loading pictures
        self.img_game_chrono = pygame.image.load('assets/image/game_chrono.png').convert_alpha()
        self.img_tom = pygame.image.load('assets/image/game_tom.png').convert_alpha()
        self.img_tile_empty = pygame.image.load('assets/image/sprite/Tile_empty.png').convert_alpha()
        self.img_tile_not_revealed = pygame.image.load('assets/image/sprite/Tile_not_revealed.png').convert_alpha()
        self.img_tile_bomb = pygame.image.load('assets/image/sprite/Tile_is_bomb.png').convert_alpha()
        self.img_picture_win = pygame.image.load('assets/image/game_win.png').convert_alpha()
        self.img_tile_flagged = pygame.image.load('assets/image/sprite/Tile_flagged.png').convert_alpha()
        self.img_tile_question_mark = pygame.image.load('assets/image/sprite/Tile_question_mark.png').convert_alpha()
        self.img_picture_lose = pygame.image.load('assets/image/game_lose.png').convert_alpha()
        self.img_best = pygame.image.load('assets/image/game_best.png').convert_alpha()
        self.img_jerry = pygame.image.load('assets/image/icon-jerry1.png').convert_alpha()
        self.img_game_flag= pygame.image.load('assets/image/game_f.png').convert_alpha()

        self.add_info_json = False

    def timer_game(self):
        if self.timer:
            self.elapsed_time = time.time() - self.start_time
            minutes = int((self.elapsed_time % 3600) // 60)
            seconds = int(self.elapsed_time % 60)
            self.formatted_time = "{:02d}:{:02d}".format(minutes, seconds)

    def save_player_name(self):
        try:
            with open('player_name.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = []
        data.append((self.username, self.formatted_time))

        with open('player_name.json', 'w') as file:
            json.dump(data, file)

    def time_sec(self, time_str):
        min, sec = map(int, time_str.split(':'))

        return min * 60 + sec

    def design(self):
        # Background
        self.screen_color(self.orange)

        # Final bomb count
        self.bomb_count_final = int(self.bomb_count) - self.flag_count

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
        self.restart_game = self.button_hover(75, 370, 130, 40, self.orange1, self.white, self.orange1, self.white, "RESTART", self.font2, self.white, 25, 2, 5)

        with open("player_name.json", "r") as file:
            data = json.load(file)

        for player in data:
            player_name = player[0]
            time_str = player[1]
            time = self.time_sec(time_str)
            if time < self.best_time:
                self.player_name = player_name
                self.best_time = time

        # Best time
        self.rect_full(self.orange1, 75, 505, 130, 200, 5)
        self.rect_border(self.white, 75, 505, 130, 200, 3, 5)
        self.text_not_align(self.font2, 25,"Best", self.white, 65, 450)
        self.text_not_align(self.font2, 25," Player Time ", self.white, 25, 475)
        self.image_not_center("Winner", 20, 430, 40, 40, self.img_best)

        self.text_not_align(self.font2, 40,(str(self.best_time) + " SEC"), self.white, 25, 525)
        self.text_not_align(self.font2, 20,"by " + str(self.player_name), self.white, 25, 560)

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
        self.text_not_align(self.font3, 15, str(self.bomb_count_final), self.black, 880, 283)

        # Red flag
        self. rect_full(self.white, 890, 360, 80, 90, 5)
        self.rect_border(self.orange1, 890, 360, 80, 90, 3, 5)
        self.image_not_center("game_flag", 860, 320, 55, 55, self.img_game_flag)
        self.text_not_align(self.font3, 12, "X", self.black, 865, 385)
        self.text_not_align(self.font3, 15, str(self.flag_count), self.black, 880, 383)

        self.tile_count = int(self.size[0]*self.size[1]) - int(self.bomb_count)
        # Red tiles
        self.remaining_tiles = self.tile_count - len(self.discovered_tile)
        self. rect_full(self.white, 890, 460, 80, 90, 5)
        self.rect_border(self.orange1, 890, 460, 80, 90, 3, 5)
        self.image_not_center("tile", 868, 425, 40, 40, self.img_tile_not_revealed)
        self.text_not_align(self.font3, 12, "X", self.black, 865, 485)
        self.text_not_align(self.font3, 15, str(self.remaining_tiles), self.black, 880, 483)

        if self.tile_is_bomb == True:
            self.game_lose()
            self.game_finished = True
        if self.remaining_tiles == 0:
            self.game_win()
            if not self.add_info_json:
                self.save_player_name()
                self.add_info_json = True
                self.game_finished = True

    # Display win message
    def game_win(self):
        self.text_not_align(self.font2, 20, "You Just Won", self.green, 15, 225)
        self.text_not_align(self.font2, 20, "The Cheese ! ", self.green, 15, 250)
        self.image_not_center("picture win", 10, 120, 100, 100, self.img_picture_win)
        self.timer = False

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
                    self.board_list.append((tile_rect, (row, col)))
                    self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_not_revealed)

                    # Tile state
                    tile_state = self.tile_states.get((row, col), EMPTY)
                    # Display Flag or Question mark
                    if tile_state == FLAG:
                        self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_flagged)
                    elif tile_state == QUESTION_MARK:
                        self.image_not_center("tile", self.W // 2 - (self.size[0] * 50 // 2) + x, self.H // 2 - (self.size[1] * 50 // 2) + y, 50, 50, self.img_tile_question_mark)
                    else:
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
                        bomb_count = 0
                        for r in range(-1, 2):
                            for c in range(-1, 2):
                                if (r != 0 or c != 0) and 0 <= row + r < self.size[1] and 0 <= col + c < self.size[0]:
                                    if self.board.is_bomb_at(row + r, col + c):
                                        bomb_count += 1
                        if bomb_count > 0:
                            self.text_not_align(self.font3, 15, str(bomb_count), self.black, self.W // 2 - (self.size[0] * 50 // 2) + x + 25, self.H // 2 - (self.size[1] * 50 // 2) + y + 20)

    # Check if tile is a bomb
    def check_bomb(self, row, col):
        if self.board.is_bomb_at(row, col):
            if (row, col) not in [item[0] for item in self.discovered_tile]:
                self.discovered_tile.append(((row, col), True))
            self.tile_is_bomb = True
        else:
            self.check_adjacent_tiles(row, col)
    
    def check_adjacent_tiles(self, row, col):
        adjacent_tiles = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                        (row, col - 1),                     (row, col + 1),
                        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        
        if (row, col) not in [item[0] for item in self.discovered_tile]:
            self.discovered_tile.append(((row, col), False))
        for r, c in adjacent_tiles:
            if 0 <= r < self.size[1] and 0 <= c < self.size[0]:
                if self.board.is_bomb_at(r, c):
                    return
        for r, c in adjacent_tiles:
            if 0 <= r < self.size[1] and 0 <= c < self.size[0]:
                if not self.board.is_bomb_at(r, c) and ((r, c), False) not in self.discovered_tile:
                    self.check_adjacent_tiles(r, c)

    def game_run(self):

        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if self.rect_menu.collidepoint(event.pos):
                        self.game_running = False

                    elif self.restart_game.collidepoint(event.pos):
                        self.__init__(self.size, self.username)

                    elif event.button == 1 and not self.game_finished:  # Left click

                        for tile_rect, (row, col) in self.board_list:
                            if tile_rect.collidepoint(event.pos):
                                if not self.timer_started:
                                    self.timer_started = True
                                    self.start_time = time.time()
                                if ((row, col) not in [item[0] for item in self.discovered_tile] and self.tile_states.get((row, col), EMPTY) != FLAG and self.tile_states.get((row, col), EMPTY) != QUESTION_MARK):
                                    self.check_bomb(row, col)
                                break

                    elif event.button == 3 and not self.game_finished: # Right click - Flag, question, empty tile
                        for tile_rect, (row, col) in self.board_list:
                            if tile_rect.collidepoint(event.pos) and (row, col) not in [item[0] for item in self.discovered_tile]:
                                current_state = self.tile_states.get((row, col), EMPTY)
                                if current_state == EMPTY:
                                    self.tile_states[(row, col)] = FLAG
                                    self.flag_count += 1
                                elif current_state == FLAG:
                                    if self.flag_count > 0:
                                        self.tile_states[(row, col)] = QUESTION_MARK
                                        self.flag_count -= 1
                                else:
                                    self.tile_states[(row, col)] = EMPTY

                                self.selected_tile = (row, col)
                                break

                    elif self.rect_menu.collidepoint(event.pos):
                            self.game_running = False

            # Start Timer
            if self.timer_started:
                self.timer_game()
            self.design()
            self.draw_board()
            self.update()