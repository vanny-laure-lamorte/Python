import pygame, sys
from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen

class Home (Element, Screen): 
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        pygame.init()

    def design(self):

        # Background
        self.img_background("home1", 450, 350, 900, 700, "home1")

        # Title
        self.text_not_align(self.font1, 45,"Mines Weeper ", self.white, 300, 250)
        self.text_not_align(self.font1, 30,"—  TOM & JERRY  Version", self.white, 300, 290)


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