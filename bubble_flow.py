from pico2d import*
import game_framework
import game_world
import time
from item_potion import C_potion

# 물줄기 애니메이션 속도 계산
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 11

class C_p1_center_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x, y
        self.time = pop_time
        self.image = load_image('resource/bubbleCenter.png')
        self.frame = 0
        self.bubble_pop_sound = load_wav('resource/bubble_pop.ogg')
        self.bubble_pop_sound.set_volume(100)
        self.bubble_pop_sound.play()

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, other, group):
        if group == 'player1:centerFlow':
            game_world.remove_object(self)
        elif group == 'player2:centerFlow':
            game_world.remove_object(self)


class C_p1_up_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x, y + 60
        self.time = pop_time
        self.image = load_image('resource/bubbleUp.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        if C_potion.p1_flow_cnt == 2:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+60, 60, 60)
        elif C_potion.p1_flow_cnt == 3:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+120, 60, 60)
        elif C_potion.p1_flow_cnt == 4:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+120, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+180, 60, 60)
        elif C_potion.p1_flow_cnt == 5 :
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+120, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+180, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+240, 60, 60)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
            return self.x - 30, self.y - 30, self.x + 30, self.y + 30 + 60*(C_potion.p1_flow_cnt-1)


    def handle_collision(self, other, group):
        if group == 'player1:upFlow':
            game_world.remove_object(self)
        elif group == 'player2:upFlow':
            game_world.remove_object(self)


class C_p1_down_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x, y - 60
        self.time = pop_time
        self.image = load_image('resource/bubbleDown.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        if C_potion.p1_flow_cnt == 2:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 60, 60, 60)
        elif C_potion.p1_flow_cnt == 3:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 120, 60, 60)
        elif C_potion.p1_flow_cnt == 4:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 120, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 180, 60, 60)
        elif C_potion.p1_flow_cnt == 5:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 120, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 180, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 240, 60, 60)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30 - 60*(C_potion.p1_flow_cnt-1), self.x + 30, self.y + 30


    def handle_collision(self, other, group):
        if group == 'player1:downFlow':
            game_world.remove_object(self)
        elif group == 'player2:downFlow':
            game_world.remove_object(self)


class C_p1_left_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x - 60, y
        self.time = pop_time
        self.image = load_image('resource/bubbleLeft.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        if C_potion.p1_flow_cnt == 2:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 60, self.y, 60, 60)
        elif C_potion.p1_flow_cnt == 3:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 120, self.y, 60, 60)
        elif C_potion.p1_flow_cnt == 4:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 120, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 180, self.y, 60, 60)
        elif C_potion.p1_flow_cnt == 5:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 120, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 180, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 240, self.y, 60, 60)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30 - 60*(C_potion.p1_flow_cnt-1), self.y - 30, self.x + 30, self.y + 30


    def handle_collision(self, other, group):
        if group == 'player1:leftFlow':
            game_world.remove_object(self)
        elif group == 'player2:leftFlow':
            game_world.remove_object(self)


class C_p1_right_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x + 60, y
        self.time = pop_time
        self.image = load_image('resource/bubbleRight.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        if C_potion.p1_flow_cnt == 2:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 60, self.y, 60, 60)
        elif C_potion.p1_flow_cnt == 3:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 120, self.y, 60, 60)
        elif C_potion.p1_flow_cnt == 4:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 120, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 180, self.y, 60, 60)
        elif C_potion.p1_flow_cnt == 5:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 120, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 180, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 240, self.y, 60, 60)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30 + 60 * (C_potion.p1_flow_cnt - 1), self.y + 30

    def handle_collision(self, other, group):
        if group == 'player1:rightFlow':
            game_world.remove_object(self)
        elif group == 'player2:rightFlow':
            game_world.remove_object(self)

class C_p2_center_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x, y
        self.time = pop_time
        self.image = load_image('resource/bubbleCenter.png')
        self.frame = 0
        self.bubble_pop_sound = load_wav('resource/bubble_pop.ogg')
        self.bubble_pop_sound.set_volume(100)
        self.bubble_pop_sound.play()

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, other, group):
        if group == 'player1:centerFlow':
            game_world.remove_object(self)
        elif group == 'player2:centerFlow':
            game_world.remove_object(self)


class C_p2_up_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x, y + 60
        self.time = pop_time
        self.image = load_image('resource/bubbleUp.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        if C_potion.p2_flow_cnt == 2:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+60, 60, 60)
        elif C_potion.p2_flow_cnt == 3:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+120, 60, 60)
        elif C_potion.p2_flow_cnt == 4:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+120, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+180, 60, 60)
        elif C_potion.p2_flow_cnt == 5 :
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+120, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+180, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y+240, 60, 60)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
            return self.x - 30, self.y - 30, self.x + 30, self.y + 30 + 60*(C_potion.p2_flow_cnt-1)


    def handle_collision(self, other, group):
        if group == 'player1:upFlow':
            game_world.remove_object(self)
        elif group == 'player2:upFlow':
            game_world.remove_object(self)


class C_p2_down_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x, y - 60
        self.time = pop_time
        self.image = load_image('resource/bubbleDown.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        if C_potion.p2_flow_cnt == 2:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 60, 60, 60)
        elif C_potion.p2_flow_cnt == 3:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 120, 60, 60)
        elif C_potion.p2_flow_cnt == 4:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 120, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 180, 60, 60)
        elif C_potion.p2_flow_cnt == 5:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 60, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 120, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 180, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y - 240, 60, 60)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30 - 60*(C_potion.p2_flow_cnt-1), self.x + 30, self.y + 30


    def handle_collision(self, other, group):
        if group == 'player1:downFlow':
            game_world.remove_object(self)
        elif group == 'player2:downFlow':
            game_world.remove_object(self)


class C_p2_left_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x - 60, y
        self.time = pop_time
        self.image = load_image('resource/bubbleLeft.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        if C_potion.p2_flow_cnt == 2:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 60, self.y, 60, 60)
        elif C_potion.p2_flow_cnt == 3:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 120, self.y, 60, 60)
        elif C_potion.p2_flow_cnt == 4:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 120, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 180, self.y, 60, 60)
        elif C_potion.p2_flow_cnt == 5:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 120, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 180, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x - 240, self.y, 60, 60)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30 - 60*(C_potion.p2_flow_cnt-1), self.y - 30, self.x + 30, self.y + 30


    def handle_collision(self, other, group):
        if group == 'player1:leftFlow':
            game_world.remove_object(self)
        elif group == 'player2:leftFlow':
            game_world.remove_object(self)


class C_p2_right_flow:
    def __init__(self, x, y, pop_time):
        self.x, self.y = x + 60, y
        self.time = pop_time
        self.image = load_image('resource/bubbleRight.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        self.pop_time = time.time()

    def return_time(self):
        return self.time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 60, 60)
        if C_potion.p2_flow_cnt == 2:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 60, self.y, 60, 60)
        elif C_potion.p2_flow_cnt == 3:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 120, self.y, 60, 60)
        elif C_potion.p2_flow_cnt == 4:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 120, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 180, self.y, 60, 60)
        elif C_potion.p2_flow_cnt == 5:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 60, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 120, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 180, self.y, 60, 60)
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x + 240, self.y, 60, 60)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30 + 60 * (C_potion.p2_flow_cnt - 1), self.y + 30

    def handle_collision(self, other, group):
        if group == 'player1:rightFlow':
            game_world.remove_object(self)
        elif group == 'player2:rightFlow':
            game_world.remove_object(self)