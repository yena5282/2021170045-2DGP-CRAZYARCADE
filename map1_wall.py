import random

from pico2d import *
import tile

class Map1_wall:
    image = None
    wall_size = 60
    tile = []
    tileNum = 0

    def __init__(self):
        if Map1_wall.image == None:
            Map1_wall.image = load_image('resource/map1_wall.png')
        self.x, self.y = 55+60*random.randint(0, 13),  810-60*random.randint(0, 11)
        # if Map1_wall.tile == []:
        #     Map1_wall.tile = tile.Tiles
        #     for x in range(16, 28):
        #         Map1_wall.tile.index(x)[2] = True
        #     for x in range(46, 58):
        #         Map1_wall.tile.index(x)[2] = True
        #     for x in range(76, 88):
        #         Map1_wall.tile.index(x)[2] = True
        #     for x in range(106, 118):
        #         Map1_wall.tile.index(x)[2] = True
        #     for x in range(136, 148):
        #         Map1_wall.tile.index(x)[2] = True
        #     for x in range(166, 178):
        #         Map1_wall.tile.index(x)[2] = True

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass