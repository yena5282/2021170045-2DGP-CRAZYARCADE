from pico2d import *
import game_framework

p1Width = 65
p1Height = 70

class Player2:
    def __init__(self):
        self.x = 870
        self.y = 795
        self.face_dir = 1  # 상, 하, 좌, 우 = 0, 1, 2, 3
        self.running = False
        self.image = None
        self.image = load_image('resource/Player2.png')
        self.keyDownNum = 0
        self.frame = 0

    def update(self):
        if self.running == True:
            self.frame = (self.frame + 1) % 5
            if self.face_dir == 0:
                self.y += 1
                if self.y > 840:
                    self.y = 840
            elif self.face_dir == 1:
                self.y -= 1
                if self.y < 95:
                    self.y = 95
            elif self.face_dir == 2:
                self.x -= 1
                if self.x < 50:
                    self.x = 50
            elif self.face_dir == 3:
                self.x += 1
                if self.x > 910:
                    self.x = 910

    def draw(self):
        if self.keyDownNum == 1:
            self.running = True
            if self.face_dir == 0:
                self.image.clip_draw(self.frame * p1Width, 210, p1Width, p1Height, self.x, self.y, 85, 100)
            elif self.face_dir == 1:
                self.image.clip_draw(self.frame * p1Width, 140, p1Width, p1Height, self.x, self.y, 85, 100)
            elif self.face_dir == 2:
                self.image.clip_draw(self.frame * p1Width, 0, p1Width, p1Height, self.x, self.y, 85, 100)
            elif self.face_dir == 3:
                self.image.clip_draw(self.frame * p1Width, 70, p1Width, p1Height, self.x, self.y, 85, 100)

        else:
            self.running = False
            if self.face_dir == 0:  # 상
                self.image.clip_draw(0, 210, p1Width, p1Height, self.x, self.y, 85, 100)
            elif self.face_dir == 1:  # 하
                self.image.clip_draw(0, 140, p1Width, p1Height, self.x, self.y, 85, 100)
            elif self.face_dir == 2:  # 좌
                self.image.clip_draw(0, 0, p1Width, p1Height, self.x, self.y, 85, 100)
            elif self.face_dir == 3:  # 우
                self.image.clip_draw(0, 70, p1Width, p1Height, self.x, self.y, 85, 100)

    def handle_event(self, event):

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_UP:
                    self.keyDownNum += 1
                    self.face_dir = 0
                case pico2d.SDLK_DOWN:
                    self.keyDownNum += 1
                    self.face_dir = 1
                case pico2d.SDLK_LEFT:
                    self.keyDownNum += 1
                    self.face_dir = 2
                case pico2d.SDLK_RIGHT:
                    self.keyDownNum += 1
                    self.face_dir = 3

        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_UP:
                    self.keyDownNum -= 1
                case pico2d.SDLK_DOWN:
                    self.keyDownNum -= 1
                case pico2d.SDLK_LEFT:
                    self.keyDownNum -= 1
                case pico2d.SDLK_RIGHT:
                    self.keyDownNum -= 1
