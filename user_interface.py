import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((720, 720))

class MainMenu:
    def __init__(self, surface):
        self.surface = surface
        self.menu = pygame_menu.Menu('Menu principal', 720, 720)
        self.menu.add.button('Créer une nouvelle partie', self.create_new_game)
        self.menu.add.button('Charger une sauvegarde', self.load_save)
        self.menu.add.button('Quitter', pygame_menu.events.EXIT)

    def create_new_game(self):
        new_game_menu = NewGameMenu(self.surface)
        new_game_menu.run()

    def load_save(self):
        load_save_menu = LoadSave(self.surface)
        load_save_menu.run()

    def run(self):
        self.menu.mainloop(self.surface)

class NewGameMenu:
    def __init__(self, surface):
        self.surface = surface
        self.menu = pygame_menu.Menu('Nouvelle partie', 720, 720)
        self.menu.add.button('Joueur contre joueur', self.PVP)
        self.menu.add.button('Joueur contre IA', self.PVE)
        self.menu.add.button('Retour', pygame_menu.events.BACK)

    def PVP(self):
        pass

    def PVE(self):
        pass

    def run(self):
        self.menu.mainloop(self.surface)

    def back(self):
        new_game_menu = NewGameMenu(self.surface)
        new_game_menu.run()

class LoadSave:
    def __init__(self, surface):
        self.surface = surface
        self.menu = pygame_menu.Menu('Charger une sauvegarde', 720, 720)
        self.menu.add.button('Charger la sauvegarde 1', self.save1)
        self.menu.add.button('Charger la sauvegarde 2', self.save2)
        self.menu.add.button('Charger la sauvegarde 3', self.save3)
        self.menu.add.button('Retour', pygame_menu.events.BACK)

    def save1(self):
        pass

    def save2(self):
        pass

    def save3(self):
        pass

    def run(self):
        self.menu.mainloop(self.surface)

if __name__ == "__main__":
    main_menu = MainMenu(surface)
    main_menu.run()
