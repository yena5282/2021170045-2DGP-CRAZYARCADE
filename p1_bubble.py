from pico2d import *
import game_framework
import game_world
import time


# 물풍선 애니메이션 속도 계산
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

class C_p1_bubble:
    p1_bubble_cnt = 1
    p1_bubble_num = 0

    def __init__(self, x, y, install_time):
        self.x, self.y = x, y
        self.image = load_image('resource/bubble1.png')
        self.frame = 0
        self.time = install_time
        self.bubble_install_sound = load_wav('resource/bubble_install.ogg')
        self.bubble_install_sound.set_volume(100)
        self.bubble_install_sound.play()
        # past_time = time.time()

    def update(self):
        global current_time, bubble_install_time, past_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.install_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 45, 0, 45, 45, self.x, self.y, 60, 60)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, other, group):
        if group == 'player1:p1bubble':
            game_world.remove_object(self)
        elif group == 'player2:p1bubble':
            game_world.remove_object(self)