with open('input/day02-input.txt', 'r') as f:
    input = f.readlines()

input = [x.strip().split(' ') for x in input]

## Part 1
depth = sum(int(x[1]) for x in input if x[0] == 'down') - sum(int(x[1]) for x in input if x[0] == 'up')
hpos = sum(int(x[1]) for x in input if x[0] == 'forward')
print(depth * hpos)

## Part 2
aim = 0
hpos = 0
depth = 0
for x in input:
    if x[0] == 'down':
        aim += int(x[1])
    if x[0] == 'up':
        aim -= int(x[1])
    if x[0] == 'forward':
        hpos += int(x[1])
        depth += aim * int(x[1])
print(depth * hpos)
