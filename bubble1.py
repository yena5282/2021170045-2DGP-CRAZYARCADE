from pico2d import *
import game_world
from player1 import Player1

p1 = Player1()

class Bubble1:
    image = None
    global p1

    def __init__(self):
        if Bubble1.image == None:
            Bubble1.image = load_image('resource/bubble1.png')
        self.x, self.y = p1.x, p1.y

    def draw(self):
        self.image.clip_draw(self.frame, 0, 45, 45, self.x, self.y, 60, 60)

    def update(self):
        self.frame = (self.frame + 1) % 3

    def handle_event(self):
        pass