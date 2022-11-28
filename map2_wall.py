import random
from pico2d import *

class Map2_wall:
    image = None

    def __init__(self):
        if Map2_wall.image == None:
            Map2_wall.image = load_image('resource/map2_wall.png')
        self.x, self.y = 120+60*random.randint(0, 12),  810-60*random.randint(0, 12)

    def make_wall_list(self):
        global map2_walls
        map2_walls = [Map2_wall() for i in range(90)]
        return map2_walls

    def draw(self):
        self.image.draw(self.x, self.y, 60, 60)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, other, group):
        pass