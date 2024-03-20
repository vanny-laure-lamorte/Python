import pygame
import sys
import time

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuration de l'écran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Temps qui défile")

# Police de caractères
font = pygame.font.SysFont(None, 36)

# Boucle principale
start_time = time.time()
clock = pygame.time.Clock()

running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calcul du temps écoulé
    elapsed_time = time.time() - start_time

    # Effacer l'écran
    screen.fill(BLACK)

    # Afficher le temps écoulé
    time_text = font.render(f"Temps écoulé: {elapsed_time:.2f} secondes", True, WHITE)
    screen.blit(time_text, (20, 20))

    # Rafraîchir l'écran
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    clock.tick(30)

# Quitter Pygame
pygame.quit()
sys.exit()
