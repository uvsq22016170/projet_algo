# Import
import pygame
import pygame_menu

# Initialisation de Pygame
pygame.init()

largeur = 900
longueur = 700
surface = pygame.display.set_mode((largeur, longueur))

# Menu principal
def main_menu():
    menu_principal = pygame_menu.Menu('Menu Principal', largeur, longueur)
    menu_principal.add.button('Créer une nouvelle partie', create_new_game)
    menu_principal.add.button('Charger une sauvegarde', load_saved_game)
    menu_principal.add.button('Quitter', pygame_menu.events.EXIT)
    menu_principal.mainloop(surface)

def create_new_game():
    new_game_menu = pygame_menu.Menu('Nouvelle Partie', largeur, longueur)
    new_game_menu.add.button('Joueur contre joueur', PVP)
    new_game_menu.add.button('Joueur contre IA')
    new_game_menu.add.button('Retour', main_menu)
    new_game_menu.mainloop(surface)

def load_saved_game():
    saved_game_menu = pygame_menu.Menu('Charger une sauvegarde', largeur, longueur)
    saved_game_menu.add.button('Charger la sauvegarde 1')
    saved_game_menu.add.button('Charger la sauvegarde 2')
    saved_game_menu.add.button('Charger la sauvegarde 3')
    saved_game_menu.add.button('Retour', main_menu)
    saved_game_menu.mainloop(surface)

# Créer une nouvelle partie
def PVP():
    PVP_menu = pygame_menu.Menu('Joueur contre joueur', largeur, longueur)
    PVP_menu.add.button('Taille du quadrillage', grid_size)
    PVP_menu.add.button('Joueur qui commence', player_starts)
    PVP_menu.add.button('Lancer la partie', start_game)
    PVP_menu.add.button('Retour', create_new_game)
    PVP_menu.mainloop(surface)

def grid_size():
    pass

def player_starts():
    pass

def start_game():
    pass

if __name__ == "__main__":
    main_menu()
