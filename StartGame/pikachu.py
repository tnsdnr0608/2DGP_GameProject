from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_g, SDLK_d, SDLK_r, SDLK_SPACE, SDLK_f,draw_rectangle

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

# 점프 액션
JUMP_PIXEL_PER_METER = (10.0 / 0.3)
JUMP_SPEED_KMPH = 20.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 500.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * JUMP_PIXEL_PER_METER)

JUMP_TIME_PER_ACTION = 200
JUMP_ACTION_PER_TIME = 200.0 / JUMP_TIME_PER_ACTION
JUMP_FRAMES_PER_ACTION = 4

# 슬라이드 액션
SLIDE_PIXEL_PER_METER = (10.0 / 0.3)
SLIDE_SPEED_KMPH = 20.0
SLIDE_SPEED_MPM = (SLIDE_SPEED_KMPH * 500.0 / 60.0)
SLIDE_SPEED_MPS = (SLIDE_SPEED_MPM / 60.0)
SLIDE_SPEED_PPS = (SLIDE_SPEED_MPS * SLIDE_PIXEL_PER_METER)

SLIDE_TIME_PER_ACTION = 20
SLIDE_ACTION_PER_TIME = 20.0 / SLIDE_TIME_PER_ACTION
SLIDE_FRAMES_PER_ACTION = 3

# 스파이크 액션
SPIKE_PIXEL_PER_METER = (10.0 / 0.3)
SPIKE_SPEED_KMPH = 20.0
SPIKE_SPEED_MPM = (SPIKE_SPEED_KMPH * 500.0 / 60.0)
SPIKE_SPEED_MPS = (SPIKE_SPEED_MPM / 60.0)
SPIKE_SPEED_PPS = (SPIKE_SPEED_MPS * SPIKE_PIXEL_PER_METER)

SPIKE_TIME_PER_ACTION = 20
SPIKE_ACTION_PER_TIME = 20.0 / SPIKE_TIME_PER_ACTION
SPIKE_FRAMES_PER_ACTION = 3


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


def spike_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_f


def spike_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_f


def null(e):
    return e[0] == 'NO'


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
        # if space_down(e):
        #     pikachu.slide()
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
        # if space_down(e):
        #     pikachu.slide()
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
        if jump_up(e):
            pikachu.is_jump = 1

    @staticmethod
    def exit(pikachu, e):
        # if space_down(e):
        #     pikachu.slide()
        pass

    @staticmethod
    def do(pikachu):
        # pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pikachu.frame = (pikachu.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 4

        pikachu.y += pikachu.is_jump

        if pikachu.y >= pikachu.jump_height:
            pikachu.is_jump = -1

        if pikachu.y <= pikachu.filed:
            pikachu.is_jump = 0
            pikachu.state_machine.handle_event(('NO', 0))

    @staticmethod
    def draw(pikachu):
        if pikachu.face_dir == 1:
            pikachu.jumping_image.clip_draw(int(pikachu.frame) * 112, 0, 112, 117, pikachu.x, pikachu.y)
        elif pikachu.face_dir == -1:
            pikachu.jumping_image.clip_composite_draw(int(pikachu.frame) * 112, 0, 112, 117, 0, 'h', pikachu.x, pikachu.y, 110, 110)


class Slide:
    @staticmethod
    def enter(pikachu, e):
        if space_down(e):
            pikachu.is_slide = 1

    @staticmethod
    def exit(pikachu, e):
        if space_down(e):
            pikachu.slide()
        pass

    @staticmethod
    def do(pikachu):
        # pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        pikachu.frame = (pikachu.frame + SLIDE_FRAMES_PER_ACTION * SLIDE_ACTION_PER_TIME * game_framework.frame_time) % 3

        pikachu.x += pikachu.dir

        if pikachu.x >= pikachu.is_slide:
            pikachu.dir = -1

        if pikachu.x <= pikachu.slide_distance:
            pikachu.state_machine.handle_event(('NO', 0))

    @staticmethod
    def draw(pikachu):
        if pikachu.face_dir == 1:
            pikachu.sliding_image.clip_draw(int(pikachu.frame) * 88, 0, 88, 98, pikachu.x, pikachu.y, 110, 110)
        elif pikachu.face_dir == -1:
            pikachu.sliding_image.clip_composite_draw(int(pikachu.frame) * 88, 0, 88, 98, 0, 'h', pikachu.x,
                                                      pikachu.y, 110, 110)


class Spike:
    @staticmethod
    def enter(pikachu, e):
        if spike_down(e):
            pikachu.is_spike = True

    @staticmethod
    def exit(pikachu, e):
        # if space_down(e):
        #     pikachu.slide()
        if spike_up(e):
            pikachu.is_spike = False
            pikachu.is_jump = -1
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + SPIKE_FRAMES_PER_ACTION * SPIKE_ACTION_PER_TIME * game_framework.frame_time) % 5
        # pikachu.frame = (pikachu.frame + 1) % 5

        if pikachu.is_spike == False:
            pikachu.is_jump = 0

        # if pikachu.y <= pikachu.filed:
        #     pikachu.is_jump = 0
        #     pikachu.state_machine.handle_event(('NO', 0))

    @staticmethod
    def draw(pikachu):
        if pikachu.face_dir == 1:
            pikachu.spike_image.clip_draw(int(pikachu.frame) * 108, 0, 108, 98, pikachu.x, pikachu.y)


class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Idle, right_up: Idle, space_down: Idle, jump_down: Jump,
                   spike_down: Spike},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Slide, jump_up: Jump,
                  spike_down: Spike},
            Jump: {null: Idle, right_down: Jump, left_down: Jump, jump_down: Jump, space_down: Jump,  spike_down: Spike
            , spike_up: Idle},
            Slide: {null: Idle},
            Spike: {null: Idle},

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
        self.is_jump = 1
        self.jump_height = 350
        self.filed = 120
        self.is_slide = 0
        self.slide_distance = 140
        self.is_spike = False
        self.image = load_image('walk_sheet.png')
        self.jumping_image = load_image('jump.png')
        self.sliding_image = load_image('slide.png')
        self.spike_image = load_image('spike.png')
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
