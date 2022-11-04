from pico2d import *
import game_framework
import game_world
from map1 import Map1
from player1 import Player1
from heart import Heart

import logo_state
import title_state

map1 = None
player1 = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player1.handle_event(event)

def enter():
    global player1, map1, p1Heart1, p1Heart2, p1Heart3, p2Heart1, p2Heart2, p2Heart3
    player1 = Player1()
    map1 = Map1()
    p1Heart1, p1Heart2, p1Heart3, p2Heart1, p2Heart2, p2Heart3 = Heart(980+11+25, 625+5+25), Heart(980+11+25+50, 625+30), Heart(980+11+25+100, 625+30), Heart(980+11+25, 500+5+25), Heart(980+11+25+50, 500+5+25), Heart(980+11+25+100, 500+5+25)
    # p1Heart1 = Heart(980+11+25, 625+5+25)

    game_world.add_object(map1, 0)
    game_world.add_object(player1, 1)
    game_world.add_object(p1Heart1, 1)
    game_world.add_object(p1Heart2, 1)
    game_world.add_object(p1Heart3, 1)
    game_world.add_object(p2Heart1, 1)
    game_world.add_object(p2Heart2, 1)
    game_world.add_object(p2Heart3, 1)

    # game_world.add_object(p2Heart1, 1)


def exit():
    game_world.clear()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

    # class Map1Wall:
    #     def __init__(self):
    #         self.image = load_image('resource/Wall00.png')
    #
    #     def draw(self):
    #         self.image.draw(wallLTX+30, wallLTY-30)

    # class Map1:
    #     def __init__(self):
    #         self.image = load_image('resource/map1.png')
    #
    #     def draw(self):
    #         self.image.draw(600, 450)

    # class Player1:
    #     def __init__(self):      # player1 방향에 따라 리소스 변경
    #         self.x, self.y = 58, 95    # 플레이어1 처음 위치 : 왼쪽 아래 구석탱이
    #         self.frame = 0
    #         self.dir = 1  # 오른쪽
    #         self.image = load_image('resource/Player1.png')
    #
    #     def update(self):
    #         self.frame = (self.frame + 1) % 5
    #         if moving == True:
    #             if p1Dir == 1:
    #                 self.dir = 1
    #                 self.y += self.dir * 1
    #             elif p1Dir == 2:
    #                 self.dir = -1
    #                 self.y += self.dir * 1
    #             elif p1Dir == 3:
    #                 self.dir = -1
    #                 self.x += self.dir * 1
    #             elif p1Dir == 4:
    #                 self.dir = 1
    #                 self.x += self.dir * 1
    #
    #         elif moving == False:
    #             if p1Dir == 1:
    #                 self.dir -= 1
    #             elif p1Dir == 2:
    #                 self.dir += 1
    #             elif p1Dir == 3:
    #                 self.dir += 1
    #             elif p1Dir == 4:
    #                 self.dir -= 1
    #
    #     def draw(self):
    #         if moving == True:
    #             if p1Dir == 1:
    #                 self.image.clip_draw(self.frame * p1Width, 210, p1Width, p1Height, self.x, self.y, 80, 95)
    #             elif p1Dir == 2:
    #                 self.image.clip_draw(self.frame * p1Width, 140, p1Width, p1Height, self.x, self.y, 80, 95)
    #             elif p1Dir == 3:
    #                 self.image.clip_draw(self.frame * p1Width, 0, p1Width, p1Height, self.x, self.y, 80, 95)
    #             elif p1Dir == 4:
    #                 self.image.clip_draw(self.frame * p1Width, 70, p1Width, p1Height, self.x, self.y, 80, 95)
    #
    #         elif moving == False:
    #             if p1Dir == 1:
    #                 self.image.clip_draw(0, 210, p1Width, p1Height, self.x, self.y, 80, 95)
    #             elif p1Dir == 2:
    #                 self.image.clip_draw(0, 140, p1Width, p1Height, self.x, self.y, 80, 95)
    #             elif p1Dir == 3:
    #                 self.image.clip_draw(0, 0, p1Width, p1Height, self.x, self.y, 80, 95)
    #             elif p1Dir == 4:
    #                 self.image.clip_draw(0, 70, p1Width, p1Height, self.x, self.y, 80, 95)

    # global p1Dir, p1X, p1Y
     # global running, moving
     # events = get_events()
     # for event in events:
     #     if event.type == SDL_QUIT:
     #         game_framework.quit()
     #     elif event.type == SDL_KEYDOWN:
     #         moving = True
     #         match event.key:
     #             case pico2d.SDLK_ESCAPE:
     #                 game_framework.quit()
     #            # 플레이어1 이동 구현
     #             case pico2d.SDLK_w:
     #                 p1Dir = 1
     #             case pico2d.SDLK_s:
     #                 p1Dir = 2
     #             case pico2d.SDLK_a:
     #                 p1Dir = 3
     #             case pico2d.SDLK_d:
     #                 p1Dir = 4
     #     elif event.type == SDL_KEYUP:
     #         moving = False


# p1 = None
# running = True
# map1 = None
# moving = False

# p1Dir = 2 # p1Dir == 1 상, == 2 하, == 3 좌, == 4 우
#
# wallWidth = 60
# wallHeight = 60
#
# p1Height = 70
# p1Width = 65
#
# # 게임 내부 플레이어 이동 가능 공간 크기 박스 변수
# LTX = 25
# LTY = 840
# RBX = 930
# RBY = 60
#
# p1X, p1Y = LTX + 33, RBY + 35
#
# # 임시로 벽 하나 만든 것 -> 좌표 수정 필요
# wallLTX = LTX
# wallLTY = LTY
# wallRBX = wallLTX + 60
# wallRBY = wallLTY - 60
#
# # 게임 초기화 코드
# def enter():
#     global map1, running, map1Wall, p1
#     map1 = Map1()
#     # map1Wall = Map1Wall()
#     p1 = Player1()
#     running = True
#
# # finalization code
# def exit():
#     global map1, map1Wall, p1
#     del map1Wall
#     del map1
#     del p1
#
# def update():
#     p1.update()
# #
# def draw():
#     clear_canvas()
#     draw_world()
#     update_canvas()
#
# def draw_world():
#     map1.draw()
#     map1Wall.draw()
#     p1.draw()
#
# def pause():
#     pass
#
# def resume():
#     pass