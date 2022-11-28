import pico2d
import game_framework
import logo_state
import map1_play_state
import map2_play_state

pico2d.open_canvas(1200, 900)

# game_framework.run(logo_state)
game_framework.run(map1_play_state)

pico2d.close_canvas()