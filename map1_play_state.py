from pico2d import *
import game_framework
import game_world
import map1_wall
import skate
import bubble
import p1_bubble
import player1

# from p1_bubble import C_bubble
from map1_wall import Map1_wall
from skate import Skate
from bubble import Bubble
from map1 import Map1
# from player1 import Player1
from player2 import Player2
from heart import Heart


map1 = None
gPlayer1 = None
gPlayer2 = None
map1_walls = []
skates = []
p1_bubbles = []


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            gPlayer1.handle_event(event)
            gPlayer2.handle_event(event)
            # p1_bubble.handle_event(event)


def enter():
    global gPlayer1, gPlayer2
    global map1
    global p1Heart1, p1Heart2, p1Heart3, p2Heart1, p2Heart2, p2Heart3
    global p1_bubbles, skates, map1_walls

    gPlayer2 = Player2()
    gPlayer1 = player1.Player1()
    map1 = Map1()
    p1Heart1, p1Heart2, p1Heart3 = Heart(980+11+25, 625+5+25), Heart(980+11+25+50, 625+30), Heart(980+11+25+100, 625+30)
    p2Heart1, p2Heart2, p2Heart3 = Heart(980+11+25, 500+5+25), Heart(980+11+25+50, 500+5+25), Heart(980+11+25+100, 500+5+25)

    # player1이 설치하는 물풍선 객체 생성
    # p1_bubbles = [P1_bubble(P1_) for i in range(5)]
    # print(p1_bubbles)
    # game_world.add_objects(p1_bubbles, 2)
    # 충돌 대상 정보를 등록
    # game_world.add_collision_pairs(gPlayer1, p1_bubbles, 'player1:p1_bubble')
    # p1_bubbles = p1_bubble.C_bubble.make_bubble_list(p1_bubble.C_bubble)
    # game_world.add_objects(p1_bubbles, 2)
    # print(p1_bubbles)
    # gPlayer1 = player1.Player1(p1_bubbles)


    # 벽들 객체 생성
    map1_walls = map1_wall.Map1_wall.make_wall_list(Map1_wall)
    game_world.add_objects(map1_walls, 2)
    # 충돌 대상 정보를 등록
    game_world.add_collision_pairs(gPlayer1, map1_walls, 'player1:map1Wall')
    game_world.add_collision_pairs(gPlayer2, map1_walls, 'player2:map1Wall')


    # 리스트로 스케이트 객체 생성
    skates = skate.Skate.make_skate_list(Skate)
    # 아이템 객체는 depth 1에 생성
    game_world.add_objects(skates, 1)
    # 충돌 대상 정보를 등록
    game_world.add_collision_pairs(gPlayer1, skates, 'player1:skate')
    game_world.add_collision_pairs(gPlayer2, skates, 'player2:skate')


    # 리스트로 물풍선 아이템 객체 생성
    bubbles = bubble.Bubble.make_bubble_list(Bubble)
    # 아이템 객체는 depth 1에 생성
    game_world.add_objects(bubbles, 1)
    # 충돌 대상 정보를 등록
    game_world.add_collision_pairs(gPlayer1, bubbles, 'player1:bubble')
    game_world.add_collision_pairs(gPlayer2, bubbles, 'player2:bubble')


    game_world.add_object(map1, 0)
    game_world.add_object(gPlayer1, 3)
    game_world.add_object(gPlayer2, 3)
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
    global gPlayer1, gPlayer2
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b) == True:
            # player와 벽이 충돌했을때 충돌 처리 : 해당 진행 방향으로 나아가지 못하도록
            if group == 'player1:map1Wall':
                if gPlayer1.face_dir == 0:
                    gPlayer1.y -= (a_t - (b_b-1))
                elif gPlayer1.face_dir == 1:
                    gPlayer1.y += (b_t - (a_b-1))
                elif gPlayer1.face_dir == 2:
                    gPlayer1.x += (b_r - (a_l-1))
                elif gPlayer1.face_dir == 3:
                    gPlayer1.x -= (a_r - (b_l-1))

            elif group == 'player2:map1Wall':
                if gPlayer2.face_dir == 0:
                    gPlayer2.y -= (a_t - (b_b - 1))
                elif gPlayer2.face_dir == 1:
                    gPlayer2.y += (b_t - (a_b - 1))
                elif gPlayer2.face_dir == 2:
                    gPlayer2.x += (b_r - (a_l - 1))
                elif gPlayer2.face_dir == 3:
                    gPlayer2.x -= (a_r - (b_l - 1))

            # player와 스케이트가 충돌했을 때 충돌 처리 : 충돌한 스케이트 데이터 없애고, 충돌한 플레이어 이동 속도 증가하도록
            elif group == 'player1:skate':
                if gPlayer1.addSpeed >= 1:
                    pass
                else:
                    a.addSpeed += 0.2
                    a.handle_collision(b, group)
                    b.handle_collision(a, group)

            elif group == 'player2:skate':
                if gPlayer2.addSpeed >= 1:
                    pass
                else:
                    a.addSpeed += 0.2
                    a.handle_collision(b, group)
                    b.handle_collision(a, group)

            # player와 물풍선 아이템이 충돌했을 때 충돌 처리 : 충돌한 물풍선 아이템 데이터 없애고, 충돌한 플레이어의 사용 가능 물풍선 개수(물풍선 리스트) 증가하도록 물풍선 리스트 추가
            elif group == 'player1:bubble':
                if p1_bubble.C_bubble.p1_bubble_cnt < 5:
                    p1_bubble.C_bubble.p1_bubble_cnt += 1
                    # P1_bubble.bubbles.append([1300, 0, False])
                    a.handle_collision(a, group)
                    b.handle_collision(b, group)
                else:
                    pass

            elif group == 'player2:bubble':
                if a.bubble_num < 5:
                    # a.use_bubble.append([a.x, a.y, False])
                    a.bubble_num += 1
                    a.handle_collision(a, group)
                    b.handle_collision(b, group)
                else:
                    pass


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
    import map1_play_state

    pico2d.open_canvas()
    game_framework.run(map1_play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()