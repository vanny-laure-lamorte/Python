import pygame, json

from source.Game import Game
from source.pygame_manager.Element import Element

class Home (Element):
    def __init__(self):
        Element.__init__(self)
        self.input_name = "ENTER YOUR NAME"
        self.entry = False

        # error message
        self.error_message = False
        self.error_message_row = False
        self.error_message_col = False
        self.error_length = False
        self.input_rows = "Enter rows"
        self.input_cols = "Enter columns"

        # Loading images
        self.background_image = pygame.image.load("assets/image/home1.png")
        self.home_image = pygame.image.load("assets/image/home2.png")

        # Player info
        self.player_info_list = []

    def design(self):

        # Background
        self.img_background(475, 375, 950, 750, self.background_image)

        # Image
        self.image_not_center("home2", 250, 20, 375, 400, self.home_image)

        # Title
        self.text_not_align(self.font1, 50,"Mines Weeper ", self.white, 320, 280)
        self.text_not_align(self.font1, 30,"— TOM & JERRY Version", self.white, 320, 320)

        # Options menu
        self.input_name_rect = self.button_hover(440, 390, 240, 50, self.orange, self.white, self.orange, self.white, self.input_name, self.font2, self.white, 35, 2, 5)

        if self.error_message:
            self.text_not_align(self.font4, 12,"INVALID USERNAME", self.red, 460, 420)
        elif self.error_length:
            self.text_not_align(self.font2, 20, "You can only use 14 characters", self.red, 335, 420)

        if self.error_message_row:
            self.text_not_align(self.font4, 12,"INVALID ENTRY", self.white, 360, 690)

        if self.error_message_col:
            self.text_not_align(self.font4, 12,"INVALID ENTRY", self.white, 560, 690)

        self.btn_normal = self.button_hover(440, 470, 180, 50, self.red1, self.white, self.red2, self.white, "Normal", self.font2, self.white, 35, 2, 5)
        self.btn_expert = self.button_hover(440, 530, 180, 50, self.red1, self.white, self.red2, self.white, "Expert", self.font2, self.white, 35, 2, 5)
        self.btn_custom = self.button_hover(440, 590, 180, 50, self.red1, self.white, self.red2, self.white, "Custom", self.font2, self.white, 35, 2, 5)
        self.input_rows_rect = self.button_hover(340, 660, 180, 50, self.orange, self.white, self.orange, self.white, self.input_rows, self.font2, self.white, 35, 2, 5)
        self.input_cols_rect = self.button_hover(540, 660, 180, 50, self.orange, self.white, self.orange, self.white, self.input_cols, self.font2, self.white, 35, 2, 5)

        # Copyright
        self.text_not_align(self.font3, 15,"©", self.white, 345, 722.5)
        self.text_not_align(self.font3, 10,"Copyright 2024 | All Rights Reserved ", self.white, 360, 725)

    def run_home(self):
        home_running = True
        while home_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    home_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rows_rect.collidepoint(event.pos):
                        self.input_rows = ""
                        self.error_message_row = False
                        self.entry = True

                    elif self.input_cols_rect.collidepoint(event.pos):
                        self.input_cols = ""
                        self.error_message_col = False
                        self.entry = True

                    elif self.input_name_rect.collidepoint(event.pos):
                        if self.input_name == "ENTER YOUR NAME":
                            self.input_name = ""
                        self.entry = True
                        self.error_message = False
                        self.error_length = False

                    elif self.btn_normal.collidepoint(event.pos):
                        if self.input_name == "" or self.input_name == "ENTER YOUR NAME":
                            self.error_message = True
                            self.error_length = False
                        else:
                            g = Game((9,9), self.input_name)
                            g.game_run()
                            self.input_name = ""

                    elif self.btn_expert.collidepoint(event.pos):
                        if self.input_name == "" or self.input_name == "ENTER YOUR NAME":
                            self.error_message = True
                            self.error_length = False
                        else:
                            g = Game((13,13), self.input_name)
                            g.game_run()
                            self.input_name = ""

                    elif self.btn_custom.collidepoint(event.pos):
                        if self.input_rows == "" or self.input_rows == "Enter rows":
                            self.error_message_row = True
                        else:
                            self.error_message_row = False

                        if self.input_cols == "" or self.input_cols == "Enter columns":
                            self.error_message_col = True
                        else:
                            self.error_message_col = False

                        if self.input_name == "" or self.input_name == "ENTER YOUR NAME":
                            self.error_message = True
                        else:
                            self.error_message = False

                        if not self.error_message_row and not self.error_message_col and not self.error_message:
                            if int(self.input_rows) > 13 or int(self.input_cols) > 13:
                                pass
                            else:
                                g = Game((int(self.input_rows), int(self.input_cols)), self.input_name)
                                g.game_run()
                                self.input_name = "ENTER YOUR NAME"
                                self.input_cols = "Enter columns"
                                self.input_rows = "Enter rows"
                    else:
                        self.entry = False

                elif event.type == pygame.KEYDOWN:
                    if self.entry:
                        if event.key == pygame.K_RETURN:
                            if self.input_name:
                                self.save_player_name()

                        if event.key == pygame.K_BACKSPACE and self.input_name_rect.collidepoint(pygame.mouse.get_pos()):
                            self.input_name = self.input_name[:-1]
                            self.error_length = False

                        elif event.key == pygame.K_BACKSPACE and self.input_rows_rect.collidepoint(pygame.mouse.get_pos()):
                            self.input_rows = self.input_rows[:-1]

                        elif event.key == pygame.K_BACKSPACE and self.input_cols_rect.collidepoint(pygame.mouse.get_pos()):
                            self.input_cols = self.input_cols[:-1]

                        elif self.input_name_rect.collidepoint(pygame.mouse.get_pos()):
                            if len(self.input_name) < 10:
                                self.input_name += event.unicode
                            else:
                                self.error_length = True

                        elif self.input_rows_rect.collidepoint(pygame.mouse.get_pos()):
                            if len(self.input_rows) < 2:
                                if event.unicode.isdigit():
                                    self.input_rows += event.unicode

                        elif self.input_cols_rect.collidepoint(pygame.mouse.get_pos()):
                            if len(self.input_cols) < 2:
                                if event.unicode.isdigit():
                                    self.input_cols += event.unicode
            self.design()
            self.update()