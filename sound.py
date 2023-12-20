import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'Resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.mp3')
        self.global_music = self.path + 'global_music.mp3'
        self.npc_pain = pg.mixer.Sound(self.path + 'skeleton_pain.mp3')
        self.npc_death = pg.mixer.Sound(self.path + 'skeleton_death.mp3')

    def background_music(self):
        pg.mixer.music.load(self.global_music)
        pg.mixer.music.play(-1)