import pygame
import math

pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Paramètres de la fenêtre
largeur_fenetre = 1000
hauteur_fenetre = 800
taille_hexagone = 30

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Hexagon Grid")

# Fonction pour dessiner un hexagone
def dessiner_hexagone(x, y):
    points = []
    for angle in range(30, 391, 60):
        x_point = x + taille_hexagone * math.cos(math.radians(angle))
        y_point = y + taille_hexagone * math.sin(math.radians(angle))
        points.append((x_point, y_point))
    pygame.draw.polygon(fenetre, NOIR, points, 2)

def calculer_decalage(i, j):
    if i >= 2:
        return taille_hexagone * math.sqrt(3) * j + taille_hexagone * math.sqrt(3) / 2 + 30 + (taille_hexagone - 3) * (i - 2) + (taille_hexagone / 2) + 10 
    else:
        return taille_hexagone * math.sqrt(3) * j + (i % 2) * (taille_hexagone * math.sqrt(3) / 2) + 30

en_cours = True
while en_cours:
    fenetre.fill(BLANC)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    for i in range(11):  # Nombre de lignes
        for j in range(11):  # Nombre de colonnes
            decalage_x = calculer_decalage(i, j)
            decalage_y = taille_hexagone * 1.5 * i + 30
            dessiner_hexagone(50 + decalage_x, 50 + decalage_y)

    pygame.display.flip()

# Quitter Pygame
pygame.quit()