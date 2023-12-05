from pico2d import *
import game_world
import game_framework
from StartGame import ground

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1500.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Ball:
    image = None

    def __init__(self, x = 400, y = 600, velocity = 0.5):
        if Ball.image == None:
            Ball.image = load_image('ball.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.ball_dx = 0
        self.ball_dy = -1

    def get_bb(self):
        return self.x - 40, self.y - 35, self.x + 40, self.y + 35

    def draw(self):
        self.image.clip_draw(int(self.frame) * 42, 0, 42, 45, self.x, self.y, 80, 80)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        # self.y -= self.velocity
        # if self.y == 120:
        #     self.velocity = 0
        self.x += self.ball_dx * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.ball_dy * RUN_SPEED_PPS * game_framework.frame_time

        if self.y <= 120:
            self.y = 120
            self.ball_dy = 1
        if self.y >= 550:
            self.y = 550
            self.ball_dy = -1
        if self.x <= 50:
            self.x = 50
            self.ball_dx = 1
        if self.x >= 800:
            self.x = 800
            self.ball_dx = -1
