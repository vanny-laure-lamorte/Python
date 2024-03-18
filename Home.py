import pygame, sys
from source.pygame_manager.Element import Element
from source.pygame_manager.Screen import Screen

class Home (Element, Screen): 
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)


    def menu_option(self, font, text, y_rect ): 
        self.rect_full(self.red1, 440, y_rect, 240, 50, 5)
        self.rect_border(self.white, 440, y_rect, 240, 50, 2, 5)
        self.text_center(font, 35, text, self.white, 450, y_rect)

    # def menu_option(self): 
    #     self.rect_full(self.red1, 440, 400, 240, 50, 5)
    #     self.rect_border(self.white, 440, 400, 240, 50, 2, 5)
    #     self.text_center(self.font2, 35, "Level 1", self.white, 450, 400)
   
   
    def design(self):

        # Background
        self.img_background("home1", 450, 350, 900, 700, "home1")

        # Image
        self.image_not_center("home2", 250, 15, 400, 400, "home2")

       

        # Title
        self.text_not_align(self.font1, 50,"Mines Weeper ", self.white, 320, 280)
        self.text_not_align(self.font1, 30,"— TOM & JERRY Version", self.white, 320, 320)

        # Options menu

        self.menu_option(self.font2, "Name", 400)
        self.menu_option(self.font2, "Level 1", 460)
        self.menu_option(self.font2, "Level 2", 520)



    

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