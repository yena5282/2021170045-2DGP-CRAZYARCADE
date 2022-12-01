from pico2d import *
import game_framework
import map1_play_state
import map2_play_state

image = None
bgm = None

def enter():
    global image
    global bgm
    image = load_image('resource/title.png')
    bgm = load_music('resource/title.ogg')
    bgm.set_volume(40)
    bgm.repeat_play()


def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                game_framework.change_state(map1_play_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                game_framework.change_state(map2_play_state)
def draw():
    clear_canvas()
    image.draw(600,450)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass