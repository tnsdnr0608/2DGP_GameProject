from pico2d import *

import game_world
from ground import Ground
from pikachu import Pikachu
from cloud import Cloud
from ball import Ball


# Game object class here
import game_framework
import title


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title)
        else:
            pikachu.handle_event(event)


def init():
    global ground
    global team
    global pikachu
    global cloud
    global ball

    ground = Ground()
    game_world.add_object(ground, 0)

    cloud = Cloud()
    game_world.add_object(cloud, 0)

    ball = Ball()
    game_world.add_object(ball, 0)

    pikachu = Pikachu()
    game_world.add_object(pikachu, 1)


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
    pass


def pause():
    pikachu.wait_time = 100000000000000000000000.0
    pass


def resume():
    pikachu.wait_time = get_time()
    pass