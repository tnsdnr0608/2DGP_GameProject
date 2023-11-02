from pico2d import *
import random


class P_Map:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass


class Cloud():
    def __init__(self):
        self.x, self.y = random.randint(100, 750), random.randint(300, 600)
        self.frame = random.randint(0, 1)
        self.speed = random.randint(1, 3)
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


class Pikachu:
    def __init__(self):
        self.x, self.y = 80, 120
        self.frame = 0
        self.direction = 0
        self.image = load_image('walk_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x += 10 * self.direction

        if self.x <= 40:
            self.x = 40
        elif self.x >= 350:
            self.x = 350

    def draw(self):
        self.image.clip_draw(int(self.frame) * 110, 0, 110, 110, self.x, self.y)


class Pikachu_Right:
    def __init__(self):
        self.x, self.y = 700,  120
        self.frame = 0
        self.direction = 0
        self.image = load_image('walk_animation_right.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x += 10 * self.direction

        if self.x >= 750:
            self.x = 750
        elif self.x <= 440:
            self.x = 440

    def draw(self):
        self.image.clip_draw(int(self.frame) * 113, 0, 110, 113, self.x, self.y)


class Ball():
    def __init__(self):
        self.x, self.y = 400, 570
        self.frame = 0
        self.speed = 5
        self.image = load_image('ball.png')

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.y -= self.speed * 0.5

        if self.y <= 90:
            self.y = 90

    def draw(self):
        self.image.clip_draw(int(self.frame) * 45, 0, 45, 45, self.x, self.y, 70, 70)



def handle_events():
    global running
    global pikachu
    global pikachu_right
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_g: # 오른쪽 방향
                pikachu.direction += 1
            elif event.key == SDLK_d: # 왼쪽 방향
                pikachu.direction -= 1
            elif event.key == SDLK_RIGHT:
                pikachu_right.direction += 1
            elif event.key == SDLK_LEFT:
                pikachu_right.direction -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_g: # 오른쪽 방향
                pikachu.direction -= 1
            elif event.key == SDLK_d: # 왼쪽 방향
                pikachu.direction += 1
            elif event.key == SDLK_RIGHT:
                pikachu_right.direction -= 1
            elif event.key == SDLK_LEFT:
                pikachu_right.direction += 1

def reset_world():
    global running
    global world
    global p_map
    global cloud
    global pikachu
    global pikachu_right
    global ball

    running = True
    world = []

    p_map = P_Map()
    world.append(p_map)

    cloud = [Cloud() for i in range(10)]
    world += cloud

    pikachu = Pikachu()
    world.append(pikachu)

    pikachu_right = Pikachu_Right()
    world.append(pikachu_right)

    ball = Ball()
    world.append(ball)

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