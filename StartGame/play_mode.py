from pico2d import *

import game_world
from ground import Ground
from pikachu import Pikachu
from cloud import Cloud
from ball import Ball
from pado import Pado


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
    global pado

    ground = Ground()
    game_world.add_object(ground, 0)

    for i in range(10):
        cloud = Cloud()
        game_world.add_object(cloud, 1)

    for i in range(400):
        pado = Pado()
        game_world.add_object(pado, 1)

    ball = Ball()
    game_world.add_object(ball, 1)

    pikachu = Pikachu()
    game_world.add_object(pikachu, 1)


def update():
    game_world.update()
    if game_world.collide(pikachu, ball):
        if pikachu.is_spike:
            ball.ball_dx = pikachu.dir
            ball.ball_dy = -2
        else:
            print('COLLISION pikachu:ball')
            ball.ball_dx = -1
            ball.ball_dy = 1


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