from pico2d import load_image


class Ground:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(800 // 2, 600 // 2)

    def update(self):
        pass