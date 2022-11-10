import random
from pico2d import *

class Map1_wall:
    image = None

    def __init__(self):
        if Map1_wall.image == None:
            Map1_wall.image = load_image('resource/map1_wall.png')
        self.x, self.y = 120+60*random.randint(0, 12),  810-60*random.randint(0, 12)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass