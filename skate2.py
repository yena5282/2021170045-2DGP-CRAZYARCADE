import random
from pico2d import *
import game_world

class Skate2:
    image = None
    skates2 = []

    def __init__(self):
        if Skate2.image == None:
            Skate2.image = load_image('resource/skate.png')
        self.x, self.y = 55+60*random.randint(0, 13),  810-60*random.randint(0, 11)

    def make_skate2_list(self):
        global skates2
        skates2 = [Skate2() for i in range(12)]
        return skates2

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        if group == 'player1:skate2':
            game_world.remove_object(self)
        elif group == 'player2:skate2':
            game_world.remove_object(self)