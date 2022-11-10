from pico2d import*

class Heart:
    image = None
    p1_heart_num = 3
    p2_heart_num = 3

    def __init__(self, x, y):
        if Heart.image == None:
            Heart.image = load_image('resource/heart.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y, 80, 80)

    def update(self):
        pass


    # def remove(self):
        # self.image.remove(self)
