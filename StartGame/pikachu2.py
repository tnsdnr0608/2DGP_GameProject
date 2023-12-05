from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_KP_ENTER, SDLK_DOWN, draw_rectangle

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
JUMP_SPEED_KMPH = 40.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1300.0 / 60.0)
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
SPIKE_SPEED_MPM = (SPIKE_SPEED_KMPH * 1500.0 / 60.0)
SPIKE_SPEED_MPS = (SPIKE_SPEED_MPM / 60.0)
SPIKE_SPEED_PPS = (SPIKE_SPEED_MPS * SPIKE_PIXEL_PER_METER)

SPIKE_TIME_PER_ACTION = 60
SPIKE_ACTION_PER_TIME = 60.0 / SPIKE_TIME_PER_ACTION
SPIKE_FRAMES_PER_ACTION = 5


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_ENTER


def jump_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def jump_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def spike_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def spike_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def null(e):
    return e[0] == 'NO'


def s_null(e):
    return e[0] == 'SN'


class Idle:
    @staticmethod
    def enter(pikachu2, e):
        if pikachu2.face_dir == -1:
            pikachu2.action = 2
        elif pikachu2.face_dir == 1:
            pikachu2.action = 3
        pikachu2.dir = 0
        pikachu2.frame = 0

    @staticmethod
    def exit(pikachu2, e):
        # if space_down(e):
        #     pikachu.slide()
        pass

    @staticmethod
    def do(pikachu2):
        if pikachu2.is_spike:
            pikachu2.state_machine.handle_event(('SN', 0))
            pikachu2.is_spike = False
            pikachu2.is_jump = True
        # pikachu.frame = (pikachu.frame + 1) % 5
        pass

    @staticmethod
    def draw(pikachu2):
        pikachu2.image.clip_draw(int(pikachu2.frame) * 110, pikachu2.action * 98, 110, 98, pikachu2.x, pikachu2.y, 110, 110)


class Run:
    @staticmethod
    def enter(pikachu2, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            pikachu2.dir, pikachu2.action, pikachu2.face_dir = 1, 1, 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            pikachu2.dir, pikachu2.action, pikachu2.face_dir = -1, 0, -1

    @staticmethod
    def exit(pikachu2, e):
        # if space_down(e):
        #     pikachu.slide()
        pass

    @staticmethod
    def do(pikachu2):
        pikachu2.frame = (pikachu2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        # pikachu.frame = (pikachu.frame + 1) % 5
        # pikachu.x += pikachu.dir * 1
        pikachu2.x += pikachu2.dir * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(pikachu2):
        pikachu2.image.clip_draw(int(pikachu2.frame) * 110, pikachu2.action * 98, 110, 98, pikachu2.x, pikachu2.y)


class Jump:
    @staticmethod
    def enter(pikachu2, e):
        if jump_up(e):
            pikachu2.is_jump = 1

    @staticmethod
    def exit(pikachu2, e):
        # if space_down(e):
        #     pikachu.slide()
        pass

    @staticmethod
    def do(pikachu2):
        # pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pikachu2.frame = (pikachu2.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 4

        pikachu2.y += pikachu2.is_jump * JUMP_SPEED_PPS * game_framework.frame_time

        if pikachu2.y >= pikachu2.jump_height:
            pikachu2.is_jump = -1

        if pikachu2.y <= pikachu2.filed:
            pikachu2.is_jump = 0
            pikachu2.state_machine.handle_event(('NO', 0))

    @staticmethod
    def draw(pikachu2):
        if pikachu2.face_dir == 1:
            pikachu2.jumping_image.clip_draw(int(pikachu2.frame) * 112, 0, 112, 117, pikachu2.x, pikachu2.y)
        elif pikachu2.face_dir == -1:
            pikachu2.jumping_image.clip_composite_draw(int(pikachu2.frame) * 112, 0, 112, 117, 0, 'h', pikachu2.x, pikachu2.y, 110, 110)


class Slide:
    @staticmethod
    def enter(pikachu2, e):
        if space_down(e):
            pikachu2.is_slide = 1

    @staticmethod
    def exit(pikachu2, e):
        if space_down(e):
            pikachu2.slide()
        pass

    @staticmethod
    def do(pikachu2):
        # pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        pikachu2.frame = (pikachu2.frame + SLIDE_FRAMES_PER_ACTION * SLIDE_ACTION_PER_TIME * game_framework.frame_time) % 3

        pikachu2.x += pikachu2.dir

        if pikachu2.x >= pikachu2.is_slide:
            pikachu2.dir = -1

        if pikachu2.x <= pikachu2.slide_distance:
            pikachu2.state_machine.handle_event(('NO', 0))

    @staticmethod
    def draw(pikachu2):
        if pikachu2.face_dir == 1:
            pikachu2.sliding_image.clip_draw(int(pikachu2.frame) * 88, 0, 88, 98, pikachu2.x, pikachu2.y, 110, 110)
        elif pikachu2.face_dir == -1:
            pikachu2.sliding_image.clip_composite_draw(int(pikachu2.frame) * 88, 0, 88, 98, 0, 'h', pikachu2.x,
                                                      pikachu2.y, 110, 110)


class Spike:
    @staticmethod
    def enter(pikachu2, e):
        if spike_down(e):
            pikachu2.is_spike = True
        elif spike_up(e):
            pikachu2.is_spike = False

    @staticmethod
    def exit(pikachu2, e):
        # if space_down(e):
        #     pikachu.slide()
        if spike_up(e):
            pikachu2.is_spike = False
            pikachu2.is_jump = -1
        pass

    @staticmethod
    def do(pikachu2):
        pikachu2.frame = (pikachu2.frame + SPIKE_FRAMES_PER_ACTION * SPIKE_ACTION_PER_TIME * game_framework.frame_time) % 5
        # pikachu.frame = (pikachu.frame + 1) % 5

        if pikachu2.y == pikachu2.is_jump:
            pikachu2.state_machine.handle_event(('SN', 0))
            pikachu2.is_jump = -1

    @staticmethod
    def draw(pikachu2):
        if pikachu2.face_dir == 1:
            pikachu2.spike_image.clip_draw(int(pikachu2.frame) * 108, 0, 108, 98, pikachu2.x, pikachu2.y)
        elif pikachu2.face_dir == -1:
            pikachu2.spike_image.clip_composite_draw(int(pikachu2.frame) * 108, 0, 108, 98, 0, 'h', pikachu2.x,
                                                      pikachu2.y, 110, 110)


class StateMachine:
    def __init__(self, pikachu2):
        self.pikachu2 = pikachu2
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Idle, right_up: Idle, space_down: Idle, jump_down: Jump,
                   },
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Slide, jump_up: Jump,
                  },
            Jump: {null: Idle, right_down: Jump, left_down: Jump, jump_down: Jump, space_down: Jump,  spike_down: Spike
            , spike_up: Jump},
            Slide: {null: Idle},
            Spike: {s_null: Idle, jump_down: Jump, jump_up: Jump},

        }

    def start(self):
        self.cur_state.enter(self.pikachu2, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pikachu2)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pikachu2, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pikachu2, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.pikachu2)


class Pikachu2:
    def __init__(self):
        self.x, self.y = 700, 120
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

        if self.x >= 750:
            self.x = 750
        elif self.x <= 440:
            self.x = 440 # 오른쪽 피카츄 충돌처리

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())
