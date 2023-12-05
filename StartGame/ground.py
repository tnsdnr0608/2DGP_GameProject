from pico2d import load_image, draw_rectangle
import game_world
import game_framework


class Ground:
    def __init__(self):
        self.image = load_image('map.png')
        self.width, self.height = 800, 600

    def draw(self):
        self.image.draw(self.width // 2, self.height // 2)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 400, 70, 400, 180

    def update(self):
        pass