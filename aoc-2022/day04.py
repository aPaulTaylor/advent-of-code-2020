with open('input/day04-input.txt', 'r') as f:
    assignments = [[list(map(int, y.split('-'))) for y in x.strip().split(',')] for x in f.readlines()]

print(sum((x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or (x[0][0]>=x[1][0] and x[0][1] <= x[1][1]) for x in assignments))

print(sum((x[0][0] <= x[1][1] and x[0][1] >= x[1][0]) or (x[1][0]>=x[0][0] and x[1][1] <= x[0][0]) for x in assignments))