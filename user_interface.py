# Import
import pygame
import pygame_menu

# Initialisation de Pygame
pygame.init()

class GameMenu:
    def __init__(self):
        self.surface = pygame.display.set_mode((900, 700))
        self.largeur, self.longueur = 900, 700
        self.main_menu = pygame_menu.Menu('Menu Principal', self.largeur, self.longueur)
        self.set_main_menu()

    # Menu principal
    def set_main_menu(self):
        self.main_menu.clear()
        self.main_menu.add.button('Créer une nouvelle partie', self.create_new_game)
        self.main_menu.add.button('Charger une sauvegarde', self.load_saved_game)
        self.main_menu.add.button('Quitter', pygame_menu.events.EXIT)
        self.main_menu.mainloop(self.surface)

    def mainloop(self):
        """
        Boucle pour lancer la fenêtre depuis l'objet.
        """
        self.main_menu.mainloop(self.surface)

    def create_new_game(self):
        new_game_menu = pygame_menu.Menu('Nouvelle Partie', self.largeur, self.longueur)
        new_game_menu.add.button('Joueur contre joueur', self.pvp)
        new_game_menu.add.button('Joueur contre IA', self.pve)
        new_game_menu.add.button('Retour', self.set_main_menu)
        new_game_menu.mainloop(self.surface)

    def load_saved_game(self):
        saved_game_menu = pygame_menu.Menu('Charger une sauvegarde', self.largeur, self.longueur)
        saved_game_menu.add.button('Charger la sauvegarde 1', self.load_save_1)
        saved_game_menu.add.button('Charger la sauvegarde 2', self.load_save_2)
        saved_game_menu.add.button('Charger la sauvegarde 3', self.load_save_3)
        saved_game_menu.add.button('Retour', self.set_main_menu)
        saved_game_menu.mainloop(self.surface)

    # Créer une nouvelle partie
    def grid_size(self):
        pass

    def player_starts(self):
        pass

    def start_game(self):
        pass

    def ia_difficulty(self):
        pass

    # Joueur contre joueur
    def pvp(self):
        pvp_menu = pygame_menu.Menu('Joueur contre joueur', self.largeur, self.longueur)
        pvp_menu.add.button('Taille du quadrillage', self.grid_size)
        pvp_menu.add.button('Joueur qui commence', self.player_starts)
        pvp_menu.add.button('Lancer la partie', self.start_game)
        pvp_menu.add.button('Retour', self.create_new_game)
        pvp_menu.mainloop(self.surface)

    # Joueur contre IA
    def pve(self):
        pve_menu = pygame_menu.Menu('Joueur contre IA', self.largeur, self.longueur)
        pve_menu.add.button('Taille du quadrillage', self.grid_size)
        pve_menu.add.button('Joueur qui commence', self.player_starts)
        pve_menu.add.button('Difficulté de l\'IA', self.ia_difficulty)
        pve_menu.add.button('Lancer la partie', self.start_game)
        pve_menu.add.button('Retour', self.create_new_game)
        pve_menu.mainloop(self.surface)

    # Charger une sauvegarde
    def load_save_1(self):
        pass

    def load_save_2(self):
        pass

    def load_save_3(self):
        pass

if __name__ == "__main__":
    gm = GameMenu()
    gm.mainloop()
