from pico2d import *
import game_world
import random
import game_framework


class Pado:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), random.randint(1, 3)
        self.frame = random.randint(1, 2)
        self.speed = random.randint(1, 1)
        self.image = load_image('pado.png')
        self.direction = 1

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.y += self.speed * self.direction
        if self.y >= 10:
            self.direction = -0.1
        if self.y <= -40:
            self.direction = 0.1

    def draw(self):
        self.image.draw(self.x, self.y)