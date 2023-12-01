# 게임 월드 관리 모듈

objects = [[], []]


# 월드에 객체를 넣는 함수
def add_object(o, depth = 0):
    objects[depth].append(o)


# 월드를 업데이트하는, 객체들을 모두 업데이트하는 함수
def update():
    for layer in objects:
        for o in layer:
            o.update()


# 월드 객체들 그리기
def render():
    for layer in objects:
        for o in layer:
            o.draw()


def clear():
    for layer in objects:
        layer.clear()


def collide(a, b): # ball과 pikachu의 충돌처리
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True