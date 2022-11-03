from pico2d import*
import game_world

class Heart:
    image = None
    p1_heart_num = 3
    p2_heart_num = 3

    def __init__(self):
        if Heart.image == None:
            Heart.image = load_image('resource/heart.png')
        # self.x, self.y = x, y

    def draw(self):
        self.image.draw(self)

    # def remove(self):
        # self.image.remove(self)

    def update(self):
        pass