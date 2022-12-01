from pico2d import*
import game_framework
import game_world


class C_bubble_flow:
    p1_flow_cnt = 1

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.up_image = load_image('resource/')