# target area: x=209..238, y=-86..-59

def test_shot(v):
    pos = [0, 0]
    while True:
        pos = [sum(x) for x in list(zip(pos,v))]
        if pos[0] > 238 or pos[1] < -86:
            return False
        if pos[0] >= 209 and pos[1] <= -59:
            return True
        v = [(v[0] - 1 if v[0] > 0 else 0), v[1] - 1]

print(sum(sum(test_shot([vx, vy]) for vx in range(20, 239)) for vy in range(-86, 86)))
