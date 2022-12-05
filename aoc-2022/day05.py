with open('input/day05-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

stacks_input=[x[1::4] for x in input[:8]]

stacks = [[x[i] for x in stacks_input][::-1] for i in range(9)]
stacks = [[x for x in st if x!=' '] for st in stacks]

moves = input[10:]
moves = [list(map(int, x.split(' ')[1::2])) for x in moves]

# part 1
#for mv in moves:
#    for i in range(mv[0]):
#        stacks[mv[2]-1].append(stacks[mv[1]-1].pop())

# part 2
for mv in moves:
    tempstack=[]
    for i in range(mv[0]):
        tempstack.append(stacks[mv[1]-1].pop())
    for i in range(mv[0]):
        stacks[mv[2]-1].append(tempstack.pop())

print(''.join([s[-1] for s in stacks]))