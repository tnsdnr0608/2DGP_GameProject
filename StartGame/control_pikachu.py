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
        self.is_jumping = False
        self.jump_speed = 10
        self.jump_height = 200
        self.y_before_jump = 0
        self.gravity = 1
        self.fall_speed = 0
        self.image = load_image('walk_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 5

        if self.is_jumping:
            self.y += self.jump_speed

            if self.y >= self.y_before_jump + self.jump_height:
                self.is_jumping = False
                self.fall_speed = 0
        else:
            self.fall_speed += self.gravity
            self.y -= self.fall_speed

            if self.y <= 120:
                self.y = 120
                self.fall_speed = 0

        self.x += 10 * self.direction

        if self.x <= 40:
            self.x = 40
        elif self.x >= 350:
            self.x = 350

        if not self.is_jumping and self.y <= 120:
            self.y = 120

        if not self.is_jumping:
            self.y_before_jump = self.y

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.fall_speed = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 110, 0, 110, 110, self.x, self.y)


class Pikachu_Right:
    def __init__(self):
        self.x, self.y = 700,  120
        self.frame = 0
        self.direction = 0
        self.is_jumping2 = False
        self.jump_speed2 = 10
        self.jump_height2 = 200
        self.y_before_jump2 = 0
        self.image = load_image('walk_animation_right.png')

    def update(self):
        self.frame = (self.frame + 1) % 5

        if self.is_jumping2:
            self.y += self.jump_speed2

            if self.y >= self.y_before_jump2 + self.jump_height2:
                self.is_jumping2 = False

        self.x += 10 * self.direction

        if self.x >= 750:
            self.x = 750
        elif self.x <= 440:
            self.x = 440

    def jump2(self):
        if not self.is_jumping2:
            self.is_jumping2 = True

    def draw(self):
        self.image.clip_draw(int(self.frame) * 113, 0, 110, 113, self.x, self.y)


class Ball():
    def __init__(self):
        self.x, self.y = 400, 570
        self.frame = 0
        self.speed = 5
        self.image = load_image('ball.png')

    def check_collision(self, target):
        if{
            self.x - 35 < target.x + 55 and
            self.x + 35 > target.x - 55 and
            self.y - 35 < target.y + 55 and
            self.y + 35 > target.y - 55
        }:
            return True

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
            elif event.key == SDLK_r:  # Jump when the space key is pressed
                pikachu.jump()
            elif event.key == SDLK_UP:
                pikachu_right.jump2()
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

    if ball.check_collision(pikachu):
        # Handle collision with Pikachu (e.g., reset the ball's position)
        ball.y = 570

        # Check for collision with Pikachu_Right
    if ball.check_collision(pikachu_right):
        # Handle collision with Pikachu_Right (e.g., reset the ball's position)
        ball.y = 570


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