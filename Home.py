import pygame, sys
from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen

class Home (Element, Screen): 
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
   
    def design(self):

        # Background
        self.img_background("home1", 450, 350, 900, 700, "home1")

        # Image
        self.image_not_center("home2", 250, 20, 400, 400, "home2")       

        # Title
        self.text_not_align(self.font1, 50,"Mines Weeper ", self.white, 320, 280)
        self.text_not_align(self.font1, 30,"— TOM & JERRY Version", self.white, 320, 320)

        # Options menu
        self.button_hover("Name", 440, 400, 240, 50, self.red1, self.white, self.yellow, self.white, "Name", self.font2, self.white, 35, 2, 5)
        self.button_hover("Level 1", 440, 460, 240, 50, self.red1, self.white, self.yellow, self.white, "Level 1", self.font2, self.white, 35, 2, 5)
        self.button_hover("Level 2", 440, 520, 240, 50, self.red1, self.white, self.yellow, self.white, "Level 2", self.font2, self.white, 35, 2, 5)

        # Copyright  
        self.text_not_align(self.font3, 15,"©", self.white, 345, 678)
     
        self.text_not_align(self.font3, 10,"Copyright 2024 | All Rights Reserved ", self.white, 360, 680)

    def run_home(self):
        home_running = True
        while home_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    home_running = False
                    
            self.design()
            self.update()
        
      
home = Home()
home.run_home()