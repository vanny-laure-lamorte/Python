import pygame

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
        self.error_grid = False
        self.error_premium = False

        # Loading images
        self.background_image = pygame.image.load("assets/image/home1.png")
        self.home_image = pygame.image.load("assets/image/home2.png")

        self.image_premium = pygame.image.load("assets/image/home_premium.png")

        self.image_lock = pygame.image.load("assets/image/icon-jerry.png")
        self.image_lock = pygame.transform.scale(self.image_lock, (50, 50))

        self.image_lock1 = pygame.image.load("assets/image/icon-jerry1.png")
        self.image_lock1 = pygame.transform.scale(self.image_lock1, (50, 50))

        # Player info
        self.player_info_list = []

        # Jump lock
        self.jumping = False
        self.jump_count = 10
        self.jump_timer = 0
        self.jump_cooldown = 30
        self.clock = pygame.time.Clock()

        self.jerry_x = 680 //2 - self.image_lock.get_width() // 2
        self.jerry_y = 880 - self.image_lock.get_height()

        self.jerry_y = 880 - self.image_lock1.get_height()


        self.jerry1_x = 1220 //2 - self.image_lock1.get_width() // 2

        self.clock = pygame.time.Clock()

    # def jump(self):

    def premium(self):

        current_time = pygame.time.get_ticks()
        if current_time - self.jump_timer  > self.jump_cooldown:
            self.jumping = True
            self.jump_timer  = current_time

        if self.jumping:
            if self.jump_count >= -4:
                self.jerry_y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 4
                self.jumping = False

        self.Window.blit(self.image_lock, (self.jerry_x, self.jerry_y))
        self.Window.blit(self.image_lock1, (self.jerry1_x, self.jerry_y))

        self.img_center("premium", self.W//2, 670, 180, 180,self.image_premium )
        self.text_center(self.font2, 20," Unlock all levels", self.white, self.W//2, 658)
        self.text_center(self.font2, 25,"PREMIUM 9.99 $", self.blue, self.W//2, 685)

    def design(self):

        # Background
        self.img_background(475, 375, 950, 750, self.background_image)

        # Image
        # self.image_not_center("home2", 250, 20, 375, 400, self.home_image)
        self.img_center("home2", self.W//2, 205, 375, 400,self.home_image)

        # Title
        self.text_center(self.font1, 50,"Mines Weeper ", self.white, self.W//2, 280)
        self.text_center(self.font1, 30,"— TOM & JERRY Version", self.white, self.W//2, 320)

        # Options menu
        self.input_name_rect = self.button_hover(self.W//2, 375, 240, 50, self.orange, self.white, self.orange, self.white, self.input_name, self.font2, self.white, 35, 2, 5)

        if self.error_message:
            self.text_not_align(self.font4, 12,"INVALID USERNAME", self.red, 495, 403)
        elif self.error_length:
            self.text_not_align(self.font4, 12, "YOU CAN ONLY USE 14 CHARACTERS", self.red, 410, 403)

        if self.error_message_row:
            self.text_not_align(self.font4, 12,"INVALID ENTRY", self.white, 610, 580)

        if self.error_message_col:
            self.text_not_align(self.font4, 12,"INVALID ENTRY", self.white, 610, 550)

        self.btn_normal = self.button_hover(self.W//2, 450, 180, 50, self.red1, self.white, self.red2, self.white, "Normal", self.font2, self.white, 35, 2, 5)
        self.btn_expert = self.button_hover(self.W//2, 510, 180, 50, self.red1, self.white, self.red2, self.white, "Expert", self.font2, self.white, 35, 2, 5)
        self.btn_custom = self.button_hover(430, 570, 140, 55, self.red1, self.white, self.red2, self.white, "Custom", self.font2, self.white, 35, 2, 5)
        self.input_cols_rect = self.button_hover(550, 555, 90, 25, self.red1, self.white, self.red2, self.white, self.input_cols, self.font3, self.white, 10, 2, 5)
        self.input_rows_rect = self.button_hover(550, 585, 90, 25, self.red1, self.white, self.red2, self.white, self.input_rows, self.font3, self.white, 10, 2, 5)


        if self.error_grid:
            self.text_not_align(self.font4, 12,"Min columns and row: 4", self.red, 360, 600)

        if self.error_premium:
            if int(self.input_rows) < 13 and int(self.input_cols) < 13:
                self.error_premium = False
            self.premium()

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
                        if self.input_rows == "Enter rows":
                            self.input_rows = ""
                        self.error_message_row = False
                        self.entry = True

                    elif self.input_cols_rect.collidepoint(event.pos):
                        if self.input_cols == "Enter columns":
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
                            self.input_name, self.input_cols, self.input_rows = "ENTER YOUR NAME", "Enter columns", "Enter rows"


                    elif self.btn_expert.collidepoint(event.pos):
                        if self.input_name == "" or self.input_name == "ENTER YOUR NAME":
                            self.error_message = True
                            self.error_length = False
                        else:
                            g = Game((13,13), self.input_name)
                            g.game_run()
                            self.input_name, self.input_cols, self.input_rows = "ENTER YOUR NAME", "Enter columns", "Enter rows"

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
                            if int(self.input_cols) < 4 or int(self.input_rows) < 4:
                                self.error_grid = True

                            elif int(self.input_cols) > 13 or int(self.input_rows) > 13:
                                self.error_premium = True
                            else:
                                g = Game((int(self.input_rows), int(self.input_cols)), self.input_name)
                                g.game_run()
                                self.input_name, self.input_cols, self.input_rows = "ENTER YOUR NAME", "Enter columns", "Enter rows"

                    else:
                        self.entry = False

                elif event.type == pygame.KEYDOWN:
                    if self.entry:

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
                                    self.error_grid = False

                        elif self.input_cols_rect.collidepoint(pygame.mouse.get_pos()):
                            if len(self.input_cols) < 2:
                                if event.unicode.isdigit():
                                    self.input_cols += event.unicode
                                    self.error_grid = False

            self.design()
            self.update()