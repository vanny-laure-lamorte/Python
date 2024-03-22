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
        self.error_length = False

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


    def jump(self): 
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

    def premium(self):
        self.img_center("premium", self.W//2, 670, 180, 180,self.image_premium )
        self.text_center(self.font2, 20," Unlock all levels", self.white, self.W//2, 658)
        self.text_center(self.font2, 25,"PREMIUM", self.blue, self.W//2, 685)

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
            self.text_not_align(self.font4, 12,"INVALID USERNAME", self.red, 460, 400)
        elif self.error_length: 
            self.text_not_align(self.font2, 20, "You can only use 14 characters", self.red, 335, 405)

        self.btn_normal = self.button_hover(self.W//2, 450, 180, 50, self.red1, self.white, self.red2, self.white, "Normal", self.font2, self.white, 35, 2, 5)
        self.btn_expert = self.button_hover(self.W//2, 510, 175, 50, self.red1, self.white, self.red2, self.white, "Expert", self.font2, self.white, 35, 2, 5)
        self.button_hover(430, 570, 140, 55, self.red1, self.white, self.red2, self.white, "Custom", self.font2, self.white, 35, 2, 5)
        self.button_hover(550, 555, 65, 25, self.red1, self.white, self.red2, self.white, "Columns", self.font3, self.white, 10, 2, 5)
        self.button_hover(550, 585, 65, 25, self.red1, self.white, self.red2, self.white, "Rows", self.font3, self.white, 10, 2, 5)

        self.premium()
           
    def player_info(self): 
        try:
            with open('player_name.json', 'r') as file:
                self.player_info_list = json.load(file)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def run_home(self):
        home_running = True
        while home_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    home_running = False            

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_name_rect.collidepoint(event.pos):
                        if self.input_name == "ENTER YOUR NAME":
                            self.input_name = ""
                        self.entry = True
                        self.error_message = False
                        self.entry = 1
                        self.error_length = False
                        
                    elif self.btn_normal.collidepoint(event.pos):
                        if self.input_name == "" or self.input_name == "ENTER YOUR NAME":
                            self.error_message = True
                      
                        else:
                            g = Game((9,9), self.input_name)
                            g.game_run()
                            self.input_name = ""


                    elif self.btn_expert.collidepoint(event.pos):
                        if self.input_name == "" or self.input_name == "ENTER YOUR NAME":
                            self.error_message = True
                   
                        else:
                            g = Game((13,13), self.input_name)
                            g.game_run()
                            self.input_name = ""
                    else:
                        self.entry = False

                elif event.type == pygame.KEYDOWN and self.entry:
                    
                    if event.key == pygame.K_RETURN:
                        if self.input_name:
                            self.save_player_name()

                    if event.key == pygame.K_BACKSPACE:
                        self.input_name = self.input_name[:-1]
                        self.error_length = False
                    else:
                        if event.unicode and len(self.input_name) < 14:
                            self.input_name += event.unicode

                        else:
                            self.error_length = True
           

            self.design()
            self.player_info()
            self.jump()
            self.update()


