from pico2d import load_image, draw_rectangle, load_music
import game_world
import game_framework


class Ground:
    def __init__(self):
        self.font = None
        self.image = load_image('map.png')
        self.width, self.height = 800, 600
        self.bgm = load_music('bgm.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()


    def draw(self):
        self.image.draw(self.width // 2, self.height // 2)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 400, 70, 400, 200

    def update(self):
        pass
