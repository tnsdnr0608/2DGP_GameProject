from pico2d import *
import game_world
import random
import game_framework


class Cloud:
    def __init__(self):
        self.x, self.y = random.randint(100, 750), random.randint(300, 600)
        self.frame = random.randint(1, 5)
        self.speed = random.randint(1, 1)
        self.image = load_image('cloud.png')
        self.direction = 1

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.x += self.speed * self.direction
        if self.x >= 750:
            self.direction = -1
        if self.x <= 50:
            self.direction = 1

    def draw(self):
        self.image.draw(self.x, self.y)