from pico2d import *


class P_Map:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global world
    global p_map
    running = True
    world = []

    p_map = P_Map()
    world.append(p_map)


def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas(800, 600)
reset_world()


while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


close_canvas()