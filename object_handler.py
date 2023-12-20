from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'Resources/sprites/npc/'
        self.static_sprite_path = 'Resources/sprites/static_sprites/'
        self.animated_sprite_path = 'Resources/sprites/animated_sprites/'

        add_sprite = self.add_sprite
        add_npc = self.add_npc

        # Debugging Sprites
        # add_sprite(SpriteObject(game))
        # add_sprite(AnimatedSprite(game))

        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'barrel/barrel.png', pos=(1.2, 1.2), scale=0.5, shift=0.8))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'barrel/barrel.png', pos=(1.2, 7.8), scale=0.5, shift=0.8))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'barrel/barrel.png', pos=(8.2, 1.2), scale=0.5, shift=0.8))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'torches/red_torch_1.png', pos=(1.2, 1.2),
                                  scale=1.0, shift=0.1))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'effigies/effigy_1.png', pos=(5.0, 2.0), scale=0.9, shift=0.2))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'barrel/barrel.png', pos=(1.2, 1.2), scale=0.5, shift=0.8))

        add_npc(NPC(game))


    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]


    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, sprite):
        self.npc_list.append(sprite)

