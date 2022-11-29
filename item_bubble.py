from pico2d import *
import game_world
import random

# from player1 import Player1
# from player2 import Player2

# p1 = Player1()
# p2 = Player2()

class C_item_bubble:
    image = None
    bubbles = [[0, 0, False]]
    # global p1

    def __init__(self):
        if self.image == None:
            self.image = load_image('resource/bubble.png')
        self.x, self.y = 55+60*random.randint(0, 13),  810-60*random.randint(0, 11)

    def make_bubble_list(self):
        global bubbles
        bubbles = [C_item_bubble() for i in range(12)]
        return bubbles

    def draw(self):
        # self.image.clip_draw(self.frame, 0, 45, 45, self.x, self.y, 60, 60)
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        # self.frame = (self.frame + 1) % 3
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        if group == 'player1:bubble':
            game_world.remove_object(self)
        elif group == 'player2:bubble':
            game_world.remove_object(self)