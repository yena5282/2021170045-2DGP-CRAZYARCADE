from pico2d import*
import random
import game_world

class C_potion:
    image = None
    potions = []
    p1_flow_cnt = 1
    p2_flow_cnt = 1

    def __init__(self):
        if self.image == None:
            self.imgae = load_image('resource/potion.png')
        self.x, self.y = 55+60*random.randint(0, 13),  810-60*random.randint(0, 11)

    def make_potion_list(self):
        global potions
        potions = [C_potion() for i in range(10)]
        return potions

    def draw(self):
        self.imgae.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        if group == 'player1:potion':
            game_world.remove_object(self)
        elif group == 'player2:potion':
            game_world.remove_object(self)