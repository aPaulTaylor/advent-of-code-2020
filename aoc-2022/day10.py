with open('input/day10-input.txt', 'r') as f:
    program = [x.strip().split(' ') for x in f.readlines()]

cur_cycle=0
X=1
X_sum=0

for instr in program:
    cur_cycle+=1
    if cur_cycle in [20,60,100,140,180,220]:
        X_sum+=(X*cur_cycle)
    if instr[0]=='addx':
        cur_cycle += 1
        if cur_cycle in [20, 60, 100, 140, 180, 220]:
            X_sum += (X*cur_cycle)
        X+=int(instr[1])

print(X_sum)

cur_cycle=0
X=1
display=''

display = display + ('█' if abs(X-(cur_cycle % 40)) < 2 else ' ')
for instr in program:
    cur_cycle+=1
    display = display + ('█' if abs(X-(cur_cycle % 40)) < 2 else ' ')
    if instr[0]=='addx':
        X += int(instr[1])
        cur_cycle += 1
        display = display + ('█' if abs(X - (cur_cycle % 40)) < 2 else ' ')

for i in range(0,len(display),40):
    print(display[i:i+40])