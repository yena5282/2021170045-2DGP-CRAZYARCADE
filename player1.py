from pico2d import *
import game_framework
import game_world

import p1_bubble

p1Width = 65
p1Height = 70

# player1 달리는 속도 계산
runPixel = 10.0
PIXEL_PER_METER = (runPixel / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# player1 애니메이션 속도 계산
TIME_PER_PLAYER_ACTION = 0.5
PLAYER_ACTION_PER_TIME = 1.0 / TIME_PER_PLAYER_ACTION
FRAMES_PER_PLAYER_ACTION = 5

p1_bubbles = []

class Player1:
    def __init__(self):
        # global p1_bubbles
        global p1_bubbles

        self.x = 55
        self.y = 85
        self.face_dir = 1  # 상, 하, 좌, 우 = 0, 1, 2, 3
        self.running = False
        self.player_image = load_image('resource/Player1.png')
        self.keyDownNum = 0
        self.frame = 0
        self.addSpeed = 0.0
        # p1_bubbles = bubble_list


    def update(self):
        if self.running == True:
            self.frame = (self.frame + FRAMES_PER_PLAYER_ACTION * PLAYER_ACTION_PER_TIME * game_framework.frame_time) % 5
            if self.face_dir == 0:
                self.y += (RUN_SPEED_PPS * game_framework.frame_time) + self.addSpeed
                if self.y > 840:
                    self.y = 840
            elif self.face_dir == 1:
                self.y -= (RUN_SPEED_PPS * game_framework.frame_time) + self.addSpeed
                if self.y < 95:
                    self.y = 95
            elif self.face_dir == 2:
                self.x -= (RUN_SPEED_PPS * game_framework.frame_time) + self.addSpeed
                if self.x < 50:
                    self.x = 50
            elif self.face_dir == 3:
                self.x += (RUN_SPEED_PPS * game_framework.frame_time) + self.addSpeed
                if self.x > 910:
                    self.x = 910

    def draw(self):
        if self.keyDownNum == 1:
            self.running = True
            if self.face_dir == 0:
                self.player_image.clip_draw(int(self.frame) * p1Width, 210, p1Width, p1Height, self.x, self.y, 80, 95)
            elif self.face_dir == 1:
                self.player_image.clip_draw(int(self.frame) * p1Width, 140, p1Width, p1Height, self.x, self.y, 80, 95)
            elif self.face_dir == 2:
                self.player_image.clip_draw(int(self.frame) * p1Width, 0, p1Width, p1Height, self.x, self.y, 80, 95)
            elif self.face_dir == 3:
                self.player_image.clip_draw(int(self.frame) * p1Width, 70, p1Width, p1Height, self.x, self.y, 80, 95)
        # if
        else:
            self.running = False
            if self.face_dir == 0:  # 상
                self.player_image.clip_draw(0, 210, p1Width, p1Height, self.x, self.y, 80, 95)
            elif self.face_dir == 1:  # 하
                self.player_image.clip_draw(0, 140, p1Width, p1Height, self.x, self.y, 80, 95)
            elif self.face_dir == 2:  # 좌
                self.player_image.clip_draw(0, 0, p1Width, p1Height, self.x, self.y, 80, 95)
            elif self.face_dir == 3:  # 우
                self.player_image.clip_draw(0, 70, p1Width, p1Height, self.x, self.y, 80, 95)

        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_feet_xy())

    def handle_event(self, event):
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            match event.key:
                # 플레이어 이동
                case pico2d.SDLK_w:
                    self.keyDownNum += 1
                    self.face_dir = 0
                case pico2d.SDLK_s:
                    self.keyDownNum += 1
                    self.face_dir = 1
                case pico2d.SDLK_a:
                    self.keyDownNum += 1
                    self.face_dir = 2
                case pico2d.SDLK_d:
                    self.keyDownNum += 1
                    self.face_dir = 3
                # 물풍선 설치
                case pico2d.SDLK_SPACE:
                    if p1_bubble.C_bubble.p1_bubble_cnt > p1_bubble.C_bubble.p1_bubble_num:
                        p1_bubbles.insert(p1_bubble.C_bubble.p1_bubble_num, (p1_bubble.C_bubble(self.x, self.y)))
                        game_world.add_object(p1_bubbles[p1_bubble.C_bubble.p1_bubble_num], 2)
                        print(p1_bubbles)
                        p1_bubble.C_bubble.p1_bubble_num += 1

        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_w:
                    self.keyDownNum -= 1
                case pico2d.SDLK_s:
                    self.keyDownNum -= 1
                case pico2d.SDLK_a:
                    self.keyDownNum -= 1
                case pico2d.SDLK_d:
                    self.keyDownNum -= 1

    def get_bb(self):
        return self.x - 17, self.y - 40, self.x + 17, self.y - 10
    def get_feet_xy(self):
        return self.x - 17, self.y - 40, self.x + 17, self.y - 30

    def get_player1_xy(self):
        return self.x, self.y

    def handle_collision(self, other, group):
        pass
