#target area: x=209..238, y=-86..-59

def test_shot(vx,vy):
    x=0
    y=0
    while True:
       x+=vx
       y+=vy
       if x> 238 or y < -86:
           return False
       if x >= 209 and y<= -59:
           return True
       vx = vx-1 if vx>0 else 0
       vy = vy-1

print(sum(sum(test_shot(vx,vy) for vx in range(20,239)) for vy in range(-86,86)))