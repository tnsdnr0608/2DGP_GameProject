from pico2d import load_image

import game_framework
import game_world
import random
import ball
import title

ground_width, ground_height = 800, 600


class Score:
    image = None

    def __init__(self, ball_in_ground):
        if Score.image == None:
            Score.image = load_image('score.png')
        self.x, self.y = 600, 500
        self.x2, self.y2 = 100, 500
        self.dir = 0
        self.score = 0
        self.score2 = 0
        self.ball_in_ground = ball_in_ground

    def draw(self):
        self.image.clip_draw(self.score * 51, 0, 50, 75, self.x, self.y)
        self.image.clip_draw(self.score2 * 51, 0, 50, 75, self.x2, self.y2)

    def update(self):
        if self.ball_in_ground.y < ball.filed and self.ball_in_ground.x < 400:
            self.score += 1

        if self.ball_in_ground.y < ball.filed and self.ball_in_ground.x > 400:
            self.score2 += 1

        if self.score > 3 or self.score2 > 3:
            game_framework.change_mode(title)
