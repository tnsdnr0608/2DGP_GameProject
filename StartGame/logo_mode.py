import game_framework
from pico2d import get_events, load_image, clear_canvas, update_canvas, get_time

import title

def init():
    global image
    global logo_start_time

    logo_start_time = get_time()
    image = load_image('tuk_credit.png')
    pass

def finish():
    pass

def update():
    if get_time() - logo_start_time >= 2.0:
        game_framework.change_mode(title)
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass


def handle_events():
    events = get_events()


def pause():
    pass


def resume():
    pass

