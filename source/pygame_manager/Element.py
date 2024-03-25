import pygame
from source.pygame_manager.Screen import Screen
class Element(Screen):
    def __init__(self):
        Screen.__init__(self)

        self.red = (255,0,0)
        self.red1 = (161,15,15) # Mines weeper - menu option
        self.red2 = (199,28,21) # Mines weeper - menu option
        self.white = (255, 255, 255) # Mines weeper - name game
        self.yellow = (233, 164, 41)  # Mines weeper - menu option
        self.black = (0,0,0)
        self.orange = (220, 130, 77) # Mines weeper
        self.orange1 = (231, 63, 19)  # Mines weeper - menu game details
        self.green = (36, 104, 42) # Mines weeper - win
        self.blue = (50, 130, 193) # Mines weeper - win

        # Font   
        self.font1 = "assets/font/MickeyMouseLine.otf" # Mines weeper - home
        self.font2 = "assets/font/Sunny Spells Basic.ttf" # Mines weeper - home
        self.font3 = "assets/font/Roboto-Medium.ttf" # Mines weeper - copyright
        self.font4 = "assets/font/Roboto-BoldCondensedItalic.ttf" # Mines weeper - copyright
        self.font5 = "assets/font/Jackpot.ttf" # Mines weeper - copyright

        # Image

# Def text

    def text_center(self, font, text_size, text_content, color, x, y):
        pygame.font.init()
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True,color)
        text_rect = text.get_rect(center=(x, y))
        self.Window.blit(text, text_rect)

    # Mines weeper - home
    def text_not_align(self, font, text_size, text_content, color, x, y): 
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)

    def text_center_italic(self, font, text_size, text_content, color, x, y):
        pygame.font.init()
        font_obj = pygame.font.Font(f"{font}", text_size)
        text = font_obj.render(text_content, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.Window.blit(text, text_rect)

# Def image

    def img_center(self, name, x, y, width, height, image):
        name = pygame.transform.smoothscale(image, (width, height))
        self.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))
        button = pygame.Rect((x - width//2), (y - height//2), width, height)
        return button

    # Mines weeper - Tom and Jerry Logo
    def image_not_center(self, name, x, y, width, height, image):
        name = pygame.transform.smoothscale(image,(width,height))
        self.Window.blit(name, (x,y))
        button = pygame.Rect(x, y, width, height)
        return button

    # Mines weeper - home background
    def img_background(self, x, y, width, height, image):
        image = pygame.transform.smoothscale(image, (width, height))
        self.Window.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def hover_image(self, name_rect, name, x, y, width, height, image_name, image_name_hover):
        name_rect = pygame.Rect( x - width//2, y - height//2, width, height)
        if self.is_mouse_over_button(name_rect):
            self.img_center(name, x, y, width+5, height+5, image_name_hover)
        else:
            self.img_center(name, x, y, width, height, image_name)
        return name_rect

# Def rectangle
    def rect_full(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width//2, y - height//2, width, height),0, radius)
        return button

    def rect_full_not_centered(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height),0, radius)
        return button

    def rect_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),  thickness, radius)
        return button

    # Rect border only on top
    def rect_radius_top(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),False,0, radius, radius)
        return button

    # Rect border only on bottom
    def rect_radius_bot(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),False ,0,0,0, radius, radius)
        return button

# Def Hover
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)

    # Mines weeper - home menu options
    def button_hover(self, x, y, width, height, color_full, color_border, color_hover, color_border_hover, text, font, text_color,text_size, thickness, radius): 

        button = pygame.Rect((x - width//2), (y - height//2), width, height)

        if self.is_mouse_over_button(button):
            self.rect_full(color_hover, x, y, width + 5, height + 5, radius)
            self.rect_border(color_border_hover, x, y, width + 5, height + 5, thickness, radius)
        else:
            self.rect_full(color_full, x, y, width, height, radius)
            self.rect_border(color_border, x, y, width, height, thickness, radius)
        self.text_center(font, text_size, text, text_color,  x, y)


        return button