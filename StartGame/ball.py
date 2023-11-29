from pico2d import *
import game_world


class Ball:
    image = None

    def __init__(self, x = 400, y = 600, velocity = 0.5):
        if Ball.image == None:
            Ball.image = load_image('ball.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 50, self.y - 45, self.x + 50, self.y + 45

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.velocity
        if self.y == 120:
            self.velocity = 0
