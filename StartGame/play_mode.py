from pico2d import *

import game_world
from ground import Ground
from pikachu import Pikachu
from cloud import Cloud
from ball import Ball
from pado import Pado
from pikachu2 import Pikachu2
from score import Score


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
            pikachu2.handle_event(event)


def init():
    global ground
    global team
    global pikachu
    global cloud
    global ball
    global pado
    global pikachu2
    global score

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

    pikachu2 = Pikachu2()
    game_world.add_object(pikachu2, 2)

    score = Score(ball)
    game_world.add_object(score, 1)


def update():
    game_world.update()
    if game_world.collide(pikachu, ball):
        if pikachu.is_spike:
            print('Spike pikachu:ball')
            ball.ball_dx = pikachu.dir
            ball.ball_dy = -2
        else:
            print('COLLISION pikachu:ball')
            ball.ball_dx = -1
            ball.ball_dy = 1

    if game_world.collide(pikachu2, ball):
        if pikachu2.is_spike:
            print('Spike pikachu2:ball')
            ball.ball_dx = pikachu2.dir
            ball.ball_dy = -2
        else:
            print('COLLISION pikachu2:ball')
            ball.ball_dx = -1
            ball.ball_dy = 1

    if game_world.collide(ball, ground):
        ball.ball_dx = -1 * ball.ball_dx


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