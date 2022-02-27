import pygame
pygame.init()
path=""
class SoundManagement:
    def __init__(self):
        self.sounds = {
            'eat': pygame.mixer.Sound(path+"sounds/chewing.ogg"),
            'eatf': pygame.mixer.Sound(path+"sounds/eatf.ogg"),
            'eat_super': pygame.mixer.Sound(path+"sounds/super.ogg"),
            'game_over': pygame.mixer.Sound(path+"sounds/dead.ogg"),
            'win': pygame.mixer.Sound(path+"sounds/win.ogg"),
            'game': pygame.mixer.Sound(path+"sounds/pacman.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()
    def stop(self):
        self.stop()
    def load(self, name):
        self.load(name)


