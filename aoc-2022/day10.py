with open('input/day10-input.txt', 'r') as f:
    program = [x.strip().split(' ') for x in f.readlines()]

cur_cycle = 1
X = 1
X_sum = 0
display = ''

for instr in program:
    X_sum += (X * cur_cycle) if cur_cycle in [20, 60, 100, 140, 180, 220] else 0
    display = display + ('█' if abs(X - ((cur_cycle - 1) % 40)) < 2 else ' ')
    cur_cycle += 1
    if instr[0] == 'addx':
        X_sum += (X * cur_cycle) if cur_cycle in [20, 60, 100, 140, 180, 220] else 0
        display = display + ('█' if abs(X - ((cur_cycle - 1) % 40)) < 2 else ' ')
        X += int(instr[1])
        cur_cycle += 1

print(X_sum)
for i in range(0, len(display), 40):
    print(display[i:i + 40])
