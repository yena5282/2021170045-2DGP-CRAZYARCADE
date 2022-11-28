from pico2d import *
import game_framework

from player1 import Player1

# 물풍선 애니메이션 속도 계산
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

class asdfBubble:
    image = None
    p1_bubble_cnt = 1
    is_install = False
    x, y = 1100, 0

    def __init__(self):
        self.x, self.y = asdfBubble.x, asdfBubble.y
        self.image = load_image('resource/bubble1.png')
        self.frame = 0
        # global p1_bubbles
        # self.p1_bubbles = [P1_bubble(1100, 0, False) for i in range(5)]
        # self.

    def make_bubble_list(self):
        global p1_bubbles
        p1_bubbles = [asdfBubble() for i in range(5)]
        return p1_bubbles

    def update(self):
        # if self.is_install == True:
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def draw(self):
        self.image.clip_draw(int(self.frame) * 45, 0, 45, 45, self.x, self.y, 60, 60)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30




# 스페이스바 누르면 해당 키를 눌렀을 때의 플레이어 좌표를 받아서 bubble1 리스트의 False인 내부 리스트의 x, y값에 좌표 넣어주고 False를 True로 바꿔줘야함