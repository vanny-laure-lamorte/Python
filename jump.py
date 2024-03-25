import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Saute, Jerry, Saute!")

# Charger l'image de Jerry
jerry_img = pygame.image.load("assets/image/icon-jerry.png")
jerry_img = pygame.transform.scale(jerry_img, (100, 100))  # Redimensionner l'image de Jerry

# Position initiale de Jerry
jerry_x = WINDOW_WIDTH // 2 - jerry_img.get_width() // 2
jerry_y = WINDOW_HEIGHT - jerry_img.get_height()

# Variables pour le saut
jumping = False
jump_count = 10
jump_timer = 0
jump_cooldown = 30  # Temps en millisecondes avant le prochain saut

clock = pygame.time.Clock()

# Boucle principale du jeu
while True:
    window.fill((255, 255, 255))  # Fond blanc
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Gérer le saut
    current_time = pygame.time.get_ticks()
    if current_time - jump_timer > jump_cooldown:
        jumping = True
        jump_timer = current_time
    
    if jumping:
        if jump_count >= -10:
            jerry_y -= (jump_count * abs(jump_count)) * 0.5
            jump_count -= 1
        else:
            jump_count = 10
            jumping = False
    
    # Dessiner Jerry
    window.blit(jerry_img, (jerry_x, jerry_y))
    
    pygame.display.update()
    clock.tick(30)  # Limiter le taux de rafraîchissement à 60 FPS
