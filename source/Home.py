import pygame
import json
from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen

class Home (Element, Screen):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        self.input_name = "ENTER YOUR NAME"
        self.entry = False
        # Charger les images
        self.background_image = pygame.image.load("assets/image/home1.png")
        self.home_image = pygame.image.load("assets/image/home2.png")

    def design(self):

        # Background
        self.img_background(450, 350, 900, 700, self.background_image)

        # Image
        self.image_not_center("home2", 250, 20, 400, 400, self.home_image)

        # Title
        self.text_not_align(self.font1, 50,"Mines Weeper ", self.white, 320, 280)
        self.text_not_align(self.font1, 30,"— TOM & JERRY Version", self.white, 320, 320)

        # Options menu
        self.input_name_rect = self.button_hover(440, 400, 240, 50, self.yellow, self.white, self.yellow, self.white, self.input_name, self.font2, self.white, 35, 2, 5)
        self.button_hover(440, 470, 180, 50, self.red1, self.white, self.red2, self.white, "Normal", self.font2, self.white, 35, 2, 5)
        self.button_hover(440, 530, 180, 50, self.red1, self.white, self.red2, self.white, "Expert", self.font2, self.white, 35, 2, 5)
        self.button_hover(440, 590, 180, 50, self.red1, self.white, self.red2, self.white, "Meilleur Score", self.font2, self.white, 35, 2, 5)

        # Copyright
        self.text_not_align(self.font3, 15,"©", self.white, 345, 678)

        self.text_not_align(self.font3, 10,"Copyright 2024 | All Rights Reserved ", self.white, 360, 680)

    
    def run_home(self):
        home_running = True
        while home_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    home_running = False

            

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_name_rect.collidepoint(event.pos):
                        self.entry = True
                        self.entry = 1
                        self.input_name = ""
                    else:
                        self.entry = False

                elif event.type == pygame.KEYDOWN and self.entry:
                    if event.key == pygame.K_RETURN:
                        if self.input_name:
                            self.save_player_name()

                    if event.key == pygame.K_BACKSPACE:
                        self.input_name = self.input_name[:-1]
                    else:
                        if event.unicode and len(self.input_name) < 14:
                            self.input_name += event.unicode
            self.design()
            # self.timer_game()
            self.update()

    def save_player_name(self):
        try:
            with open('player_name.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = []

        data.append(self.input_name)

        with open('player_name.json', 'w') as file:
            json.dump(data, file)
