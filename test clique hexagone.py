import pygame
import math

# Initialiser Pygame
pygame.init()

# Paramètres de l'écran
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hexagones")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Propriétés des hexagones
hex_size = 30  # Taille des hexagones
center_y = screen_height // 2  # Position y du centre des hexagones
common_side = hex_size * math.sqrt(3)  # Longueur du côté commun des hexagones

# Fonction pour dessiner un hexagone
def draw_hexagon(center_x, size, color):
    points = []
    angle_deg = 30  # Angle de rotation en degrés
    angle_rad = math.radians(angle_deg)
    for i in range(6):
        x = center_x + size * math.cos(angle_rad)
        y = center_y + size * math.sin(angle_rad)
        points.append((x, y))
        angle_rad += math.radians(60)  # Augmenter l'angle de 60 degrés pour chaque sommet suivant
    pygame.draw.polygon(screen, color, points)
    pygame.draw.polygon(screen, BLACK, points, 3)  # Contour de l'hexagone

# Fonction pour créer plusieurs hexagones avec côtés communs
def create_hexagons(num_hexagons):
    hexagones = []  # Liste pour stocker les hexagones numérotés
    total_width = num_hexagons * common_side
    start_x = (screen_width - total_width) // 2  # Position x du premier hexagone
    for i in range(num_hexagons):
        center_x = start_x + (i * common_side) + (common_side / 2)
        draw_hexagon(center_x, hex_size, WHITE)
        hexagones.append(i+1)  # Ajouter le numéro de l'hexagone à la liste
    return hexagones

# Fonction pour vérifier si un hexagone a été cliqué et afficher son numéro
def check_hexagon_clicked(mouse_pos, hexagones):
    for i, hexagon in enumerate(hexagones):
        center_x = (screen_width - (len(hexagones) * common_side)) // 2 + (i * common_side) + (common_side / 2)
        center_y = screen_height // 2  #Position y du centre des hexagones
        radius = hex_size
        distance = math.sqrt((mouse_pos[0] - center_x)**2 + (mouse_pos[1] - center_y)**2)
        if distance <= radius:
            print("Hexagone numéro", hexagon, "a été cliqué !")

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                mouse_pos = pygame.mouse.get_pos()
                check_hexagon_clicked(mouse_pos, create_hexagons(11))

    screen.fill(WHITE)

    create_hexagons(11)  # Créer 11 hexagones avec côtés communs

    pygame.display.flip()

pygame.quit()