from pico2d import *
import game_framework
import game_world
import title_state
import map1_play_state
from map1_wall import Map1_wall
from map1 import Map1
from player1 import Player1
from player2 import Player2
from heart import Heart

map1 = None
player1 = None
map1_walls = []
# map1_wall_x, map1_wall_y = 115, 750

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player1.handle_event(event)
            player2.handle_event(event)

def enter():
    global player1, player2, map1, p1Heart1, p1Heart2, p1Heart3, p2Heart1, p2Heart2, p2Heart3
    player1 = Player1()
    player2 = Player2()
    map1 = Map1()
    p1Heart1, p1Heart2, p1Heart3 = Heart(980+11+25, 625+5+25), Heart(980+11+25+50, 625+30), Heart(980+11+25+100, 625+30)
    p2Heart1, p2Heart2, p2Heart3 = Heart(980+11+25, 500+5+25), Heart(980+11+25+50, 500+5+25), Heart(980+11+25+100, 500+5+25)

    # 리스트로 벽들 객체 생성
    global map1_walls
    map1_walls = [Map1_wall() for i in range(40)]
    game_world.add_objects(map1_walls, 1)

    # 첫 번째 행부터 생성
    # global map1_wall_x, map1_wall_y

    # for map1_wall_y in range()
    # for i in range(6):
    #     for j in range(10):
    # map1_walls = [Map1_wall(map1_wall_x, map1_wall_y) for a in range(60)]
    # if(j == 5):
    #     map1_wall_x += 240
    # elif(j == 10):
    #     map1_wall_y += 120
    # else:
    #     map1_wall_x += 60



    game_world.add_object(map1, 0)
    game_world.add_object(player1, 1)
    game_world.add_object(player2, 1)
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
    import map1_play_state

    pico2d.open_canvas()
    game_framework.run(map1_play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()