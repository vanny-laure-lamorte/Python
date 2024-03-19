import pygame, sys
import time
from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen

class Home (Element, Screen): 
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        self.input_name = "ENTER YOUR NAME"

        # Timer
        self.start_time = time.time()
        self.clock = pygame.time.Clock()

    def timer_game(self):

        self.elapsed_time = time.time() - self.start_time

        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        self.formatted_time = "{:02d}:{:02d}".format(minutes, seconds)
        print (self.formatted_time)

        # Display
        self.image_not_center("game_chrono",250, 400, 60, 60, "game_chrono")
        self.text_not_align(self.font3, 15,self.formatted_time, self.black, 60, 400)

    def design(self):

        # Background
        self.img_background("home1", 450, 350, 900, 700, "home1")

        # Image
        self.image_not_center("home2", 250, 20, 400, 400, "home2")       

        # Title
        self.text_not_align(self.font1, 50,"Mines Weeper ", self.white, 320, 280)
        self.text_not_align(self.font1, 30,"— TOM & JERRY Version", self.white, 320, 320)

        # Options menu
        self.input_name_rect = self.button_hover(440, 400, 240, 50, self.yellow, self.white, self.yellow, self.white, self.input_name, self.font2, self.white, 35, 2, 5)
        self.button_hover(440, 470, 180, 50, self.red1, self.white, self.red2, self.white, "Normal", self.font2, self.white, 35, 2, 5)
        self.button_hover(440, 530, 180, 50, self.red1, self.white, self.red2, self.white, "Expert", self.font2, self.white, 35, 2, 5)

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

                elif event.type == pygame.KEYDOWN and self.entry :
                    if event.key == pygame.K_BACKSPACE:
                        self.input_name = self.input_name[:-1]
                    else:
                        if event.unicode:
                            self.input_name += event.unicode
            self.design()
            self.timer_game()
            self.update()

home = Home()
home.run_home()