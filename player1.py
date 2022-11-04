from pico2d import *
import game_world

RD, LD, UD, DD, RU, LU, UU, DU = range(8)
event_name = ['RD', 'LD', 'UD', 'DD', 'RU', 'LU', 'UU', 'DU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_w): UD,
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYDOWN, SDLK_s): DD,
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYUP, SDLK_w): UU,
    (SDL_KEYUP, SDLK_a): LU,
    (SDL_KEYUP, SDLK_s): DU,
    (SDL_KEYUP, SDLK_d): RU,
}

p1Width = 65
p1Height = 70
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.leftRight = 0
        self.upDown = 0
        self.face_dir = 1 # 처음 시작은 아래를 보고 시작하도록

    @staticmethod

    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod

    def do(self):
        pass
        # self.frame = (self.frame + 1) % 5

    @staticmethod

    def draw(self):
        if self.face_dir == 0: # 상
            self.image.clip_draw(0, 210, p1Width, p1Height, self.x, self.y, 80, 95)
        elif self.face_dir == 1: # 하
            self.image.clip_draw(0, 140, p1Width, p1Height, self.x, self.y, 80, 95)
        elif self.face_dir == 2: # 좌
            self.image.clip_draw(0, 0, p1Width, p1Height, self.x, self.y, 80, 95)
        elif self.face_dir == 3: # 우
            self.image.clip_draw(0, 70, p1Width, p1Height, self.x, self.y, 80, 95)

    @staticmethod
    def do(self):
        pass

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.leftRight += 1
        elif event == LD:
            self.leftRight -= 1
        elif event == UD:
            self.upDown += 1
        elif event == DD:
            self.upDown -= 1
        elif event == RU:
            self.leftRight -= 1
        elif event == LU:
            self.leftRight += 1
        elif event == UU:
            self.upDown -= 1
        elif event == DU:
            self.upDown += 1

    def exit(self, event):
        print('EXIT RUN')

    def do(self):
        self.frame = (self.frame + 1) % 5
        if self.face_dir == 0 or self.face_dir == 1:
            self.y += self.upDown
            self.y = clamp(60, self.y, 840)
        else:
            self.x += self.leftRight
            self.x = clamp(25, self.x, 930)


    def draw(self):
        if self.face_dir == 0:
            self.image.clip_draw(self.frame * p1Width, 210, p1Width, p1Height, self.x, self.y, 80, 95)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame * p1Width, 140, p1Width, p1Height, self.x, self.y, 80, 95)
        elif self.face_dir == 2:
            self.image.clip_draw(self.frame * p1Width, 0, p1Width, p1Height, self.x, self.y, 80, 95)
        elif self.face_dir == 3:
            self.image.clip_draw(self.frame * p1Width, 70, p1Width, p1Height, self.x, self.y, 80, 95)

# 어렵
next_state = {
    IDLE : {RU: RUN, LU: RUN, UU: RUN, DU: RUN, RD: RUN, LD: RUN, UD: RUN, DD: RUN},
    RUN : {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: IDLE, LD: IDLE, UD: IDLE, DD: IDLE}
}

class Player1:
    def __init__(self):
        self.x, self.y = 58, 105
        self.frame = 0
        self.face_dir = 1
        self.upDown = 0
        self.leftRight = 0
        self.image = load_image('resource/Player1.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('Error: ', self.cur_state, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, upDown: {self.upDown}, leftRight: {self.leftRight}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self. add_event(key_event)
