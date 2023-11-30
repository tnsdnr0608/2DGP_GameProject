from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_g, SDLK_d, SDLK_r, SDLK_SPACE, draw_rectangle

import game_framework
from ball import Ball
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_g


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_g


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def jump_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_r


def jump_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_r


class Idle:
    @staticmethod
    def enter(pikachu, e):
        if pikachu.face_dir == -1:
            pikachu.action = 2
        elif pikachu.face_dir == 1:
            pikachu.action = 3
        pikachu.dir = 0
        pikachu.frame = 0

    @staticmethod
    def exit(pikachu, e):
        if space_down(e):
            pikachu.slide()
        pass

    @staticmethod
    def do(pikachu):
        # pikachu.frame = (pikachu.frame + 1) % 5
        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 110, pikachu.action * 98, 110, 98, pikachu.x, pikachu.y)


class Run:
    @staticmethod
    def enter(pikachu, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            pikachu.dir, pikachu.action, pikachu.face_dir = 1, 1, 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            pikachu.dir, pikachu.action, pikachu.face_dir = -1, 0, -1

    @staticmethod
    def exit(pikachu, e):
        if space_down(e):
            pikachu.slide()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        # pikachu.frame = (pikachu.frame + 1) % 5
        # pikachu.x += pikachu.dir * 1
        pikachu.x += pikachu.dir * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 110, pikachu.action * 98, 110, 98, pikachu.x, pikachu.y)


class Jump:
    @staticmethod
    def enter(pikachu, e):
        pass

    @staticmethod
    def exit(pikachu, e):
        if space_down(e):
            pikachu.slide()
        pass

    @staticmethod
    def do(pikachu):
        pass

    @staticmethod
    def draw(pikachu):
        pass


class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle, jump_down: Jump},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run, jump_up: Jump},
        }

    def start(self):
        self.cur_state.enter(self.pikachu, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pikachu)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pikachu, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pikachu, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.pikachu)


class Pikachu:
    def __init__(self):
        self.x, self.y = 80, 120
        self.frame = 0
        self.action = 3
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('walk_sheet.png')
        # self.font = load_image('ENCR10B.TTF', 16)
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.item = None

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.state_machine.update()

        if self.x <= 40:
            self.x = 40
        elif self.x >= 350:
            self.x = 350  # 피카츄와 벽의 충돌처리

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

