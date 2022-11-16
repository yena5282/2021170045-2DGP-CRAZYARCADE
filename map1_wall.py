import random
from pico2d import *

class Map1_wall:
    image = None
    map1_Walls = []

    def __init__(self):
        if Map1_wall.image == None:
            Map1_wall.image = load_image('resource/map1_wall.png')
        self.x, self.y = 55+60*random.randint(0, 13),  810-60*random.randint(0, 11)

    def make_wall_list(self):
        global map1_walls
        map1_walls = [Map1_wall() for i in range(90)]
        return map1_walls

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, other, group):
        pass
