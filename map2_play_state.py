from pico2d import *
import game_framework
import game_world
import title_state
import map2_play_state
import skate2

from skate2 import Skate2
from map2_wall import Map2_wall
from map2 import Map2
from player1 import Player1
from player2 import Player2
from heart import Heart

map2 = None
player1 = None
player2 = None
map2_walls = []
skates2 = []


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
        #     game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player1.handle_event(event)
            player2.handle_event(event)

def enter():
    global player1, player2
    global map2
    global p1Heart1, p1Heart2, p1Heart3, p2Heart1, p2Heart2, p2Heart3

    player1 = Player1()
    player2 = Player2()
    map2 = Map2()
    p1Heart1, p1Heart2, p1Heart3 = Heart(980+11+25, 625+5+25), Heart(980+11+25+50, 625+30), Heart(980+11+25+100, 625+30)
    p2Heart1, p2Heart2, p2Heart3 = Heart(980+11+25, 500+5+25), Heart(980+11+25+50, 500+5+25), Heart(980+11+25+100, 500+5+25)

    # 벽들 객체 생성
    map2_walls = [Map2_wall() for i in range(90)]
    game_world.add_objects(map2_walls, 2)

    game_world.add_collision_pairs(player1, map2_walls, 'player1:map2Wall')
    game_world.add_collision_pairs(player2, map2_walls, 'player2:map2Wall')

    # 리스트로 스케이트 객체 생성
    skates2 = skate2.Skate2.make_skate2_list(Skate2)
    # 아이템 객체는 depth 1에 생성
    game_world.add_objects(skates2, 1)
    # 충돌 대상 정보를 등록
    game_world.add_collision_pairs(player1, skates2, 'player1:skate2')
    game_world.add_collision_pairs(player2, skates2, 'player2:skate2')

    game_world.add_object(map2, 0)
    game_world.add_object(player1, 3)
    game_world.add_object(player2, 3)
    game_world.add_object(p1Heart1, 2)
    game_world.add_object(p1Heart2, 2)
    game_world.add_object(p1Heart3, 2)
    game_world.add_object(p2Heart1, 2)
    game_world.add_object(p2Heart2, 2)
    game_world.add_object(p2Heart3, 2)

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
    global a_l, a_r, a_b, a_t, b_l, b_r, b_b, b_t
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b) == True:
            # player와 벽이 충돌했을때 충돌 처리 : 해당 진행 방향으로 나아가지 못하도록
            if group == 'player1:map2Wall':
                if player1.face_dir == 0:
                    player1.y -= (a_t - (b_b-1))
                elif player1.face_dir == 1:
                    player1.y += (b_t - (a_b-1))
                elif player1.face_dir == 2:
                    player1.x += (b_r - (a_l-1))
                elif player1.face_dir == 3:
                    player1.x -= (a_r - (b_l-1))

            elif group == 'player2:map2Wall':
                if player2.face_dir == 0:
                    player2.y -= (a_t - (b_b - 1))
                elif player2.face_dir == 1:
                    player2.y += (b_t - (a_b - 1))
                elif player2.face_dir == 2:
                    player2.x += (b_r - (a_l - 1))
                elif player2.face_dir == 3:
                    player2.x -= (a_r - (b_l - 1))

            # player와 스케이트가 충돌했을 때 충돌 처리 : 충돌한 스케이트 데이터 없애고, 충돌한 플레이어 이동 속도 증가하도록
            elif group == 'player1:skate2':
                if player1.addSpeed >= 0.66:
                    pass
                else:
                    a.addSpeed += 0.11
                    a.handle_collision(b, group)
                    b.handle_collision(a, group)
            elif group == 'player2:skate2':
                if player2.addSpeed >= 0.66:
                    pass
                else:
                    a.addSpeed += 0.11
                    a.handle_collision(b, group)
                    b.handle_collision(a, group)

def collide(a, b):
    global a_l, a_r, a_b, a_t, b_l, b_r, b_b, b_t
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    else:
        a_l, a_r, a_b, a_t, b_l, b_r, b_b, b_t = la, ra, ba, ta, lb, rb, bb, tb
        return True

def test_self():
    pico2d.open_canvas()
    game_framework.run(map2_play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
