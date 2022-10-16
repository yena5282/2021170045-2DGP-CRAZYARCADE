from pico2d import *
import game_framework
import logo_state
import title_state

# class Boy:
#     def __init__(self):
#         self.x, self.y = 0, 90
#         self.frame = 0
#         self.image = load_image('run_animation.png')
#
#     def update(self):
#         self.frame = (self.frame + 1) % 8
#         self.x += 1
#
#     def draw(self):
#         self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

# class Player1:
#     def __init__(self):      # player1 방향에 따라 리소스 변경
#         if p1Right == True:
#             self.image = load_image('Right.png')
#         elif p1Left == True:
#             self.image = load_image('Left.png')
#         elif p1Up == True:
#             self.image = load_image('Up.png')
#         elif p1Down == True:
#             self.image = load_image('Down.png')
#     def draw(self):
#         self.image.draw()
class Map1:
    def __init__(self):
        self.image = load_image('map1.png')

    def draw(self):
        self.image.draw(600, 450)


def handle_events():
    global p1Right, p1Left, p1Down, p1Up  # player1의 이동 방향
    global p2Right, p2Left, p2Down, p2Up  # player2의 이동 방향
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
    # delay(0.01)

# boy = None
# grass = None
running = True
map1 = None
p1Down = True
p1Up = False
p1Right = False
p1Left = False

halfBlockWidth = 30
halfBlockHeight = 30
LTX = 0
LTY = 900
RBX = 1200
RBY = 0

# 게임 초기화 코드
def enter():
    global map1, running
    # boy = Boy()
    map1 = Map1()
    running = True

# finalization code
def exit():
    global map1
#     del boy
    del map1
#
# def update():
#     boy.update()
#
def draw():
    clear_canvas()
    map1.draw()
#     boy.draw()
    update_canvas()

def update():
    pass

def pause():
    pass
def resume():
    pass