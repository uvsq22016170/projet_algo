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

# Liste pour stocker les hexagones
hexagones = []

# Fonction pour dessiner un hexagone avec numéro et l'ajouter à la liste
def dessiner_hexagone(x, y, numero):
    points = []
    for angle in range(30, 391, 60):
        x_point = x + taille_hexagone * math.cos(math.radians(angle))
        y_point = y + taille_hexagone * math.sin(math.radians(angle))
        points.append((x_point, y_point))
    pygame.draw.polygon(fenetre, NOIR, points, 2)

    # Ajouter l'hexagone à la liste
    hexagones.append((x, y, numero))

def calculer_decalage(i, j):
    if i >= 2:
        return taille_hexagone * math.sqrt(3) * j + taille_hexagone * math.sqrt(3) / 2 + 30 + (taille_hexagone - 3) * (i - 2) + (taille_hexagone / 2) + 10 
    else:
        return taille_hexagone * math.sqrt(3) * j + (i % 2) * (taille_hexagone * math.sqrt(3) / 2) + 30

def clique():
    mouse_pos = pygame.mouse.get_pos()
    for hexagone in hexagones:
        x, y, numero = hexagone
        hexagone_rect = pygame.Rect(x - taille_hexagone, y - taille_hexagone, taille_hexagone * 2, taille_hexagone * 2)
        if hexagone_rect.collidepoint(mouse_pos):
            print("Le numéro de l'hexagone est :", numero)
            return

en_cours = True
while en_cours:
    fenetre.fill(BLANC)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                clique()

    for i in range(11):  # Nombre de lignes
        for j in range(11):  # Nombre de colonnes
            decalage_x = calculer_decalage(i, j)
            decalage_y = taille_hexagone * 1.5 * i + 30
            dessiner_hexagone(50 + decalage_x, 50 + decalage_y, i * 11 + j + 1)

    pygame.display.flip()

# Quitter Pygame
pygame.quit()