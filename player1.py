from pico2d import *
import game_framework

class Player1:
    def __init__(self):      # player1 방향에 따라 리소스 변경
        self.x, self.y = 58, 95    # 플레이어1 처음 위치 : 왼쪽 아래 구석탱이
        self.frame = 0
        self.dir = 1  # 오른쪽
        self.image = load_image('resource/Player1.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        if moving == True:
            if p1Dir == 1:
                self.dir = 1
                self.y += self.dir * 1
            elif p1Dir == 2:
                self.dir = -1
                self.y += self.dir * 1
            elif p1Dir == 3:
                self.dir = -1
                self.x += self.dir * 1
            elif p1Dir == 4:
                self.dir = 1
                self.x += self.dir * 1

        elif moving == False:
            if p1Dir == 1:
                self.dir -= 1
            elif p1Dir == 2:
                self.dir += 1
            elif p1Dir == 3:
                self.dir += 1
            elif p1Dir == 4:
                self.dir -= 1

    def draw(self):
        if moving == True:
            if p1Dir == 1:
                self.image.clip_draw(self.frame * p1Width, 210, p1Width, p1Height, self.x, self.y)
            elif p1Dir == 2:
                self.image.clip_draw(self.frame * p1Width, 140, p1Width, p1Height, self.x, self.y)
            elif p1Dir == 3:
                self.image.clip_draw(self.frame * p1Width, 0, p1Width, p1Height, self.x, self.y)
            elif p1Dir == 4:
                self.image.clip_draw(self.frame * p1Width, 70, p1Width, p1Height, self.x, self.y)

        elif moving == False:
            if p1Dir == 1:
                self.image.clip_draw(0, 210, p1Width, p1Height, self.x, self.y)
            elif p1Dir == 2:
                self.image.clip_draw(0, 140, p1Width, p1Height, self.x, self.y)
            elif p1Dir == 3:
                self.image.clip_draw(0, 0, p1Width, p1Height, self.x, self.y)
            elif p1Dir == 4:
                self.image.clip_draw(0, 70, p1Width, p1Height, self.x, self.y)