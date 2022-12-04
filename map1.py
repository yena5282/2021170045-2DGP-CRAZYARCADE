from pico2d import *
import game_framework

class Map1:
    def __init__(self):
        self.image = load_image('resource/map1.png')
        self.bgm = load_music('resource/map1.ogg')
        self.bgm.set_volume(25)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(600, 450)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def handle_events(self):
        events = get_events()
        for event in events():
            if event.type == SDL_QUIT:
                game_framework.quit()

    def get_bb(self):
        return 25, 55, 930, 840