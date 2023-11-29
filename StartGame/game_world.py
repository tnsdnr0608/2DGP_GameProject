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