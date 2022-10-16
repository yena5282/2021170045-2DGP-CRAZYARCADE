import pico2d
import game_framework
import logo_state
import play_state

pico2d.open_canvas(1200, 900)

# game_framework.run(logo_state)
game_framework.run(play_state)

pico2d.close_canvas()
