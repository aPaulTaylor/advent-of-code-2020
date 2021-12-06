with open('input/day06-input.txt', 'r') as f:
    input = [int(x) for x in f.read().split(',')]

fish_counts = [sum(1 for x in input if x==i) for i in range(9)]

def iterate_fish_counts(fc):
    new_counters = [6,0,1,2,3,4,5,6,7]
    new_fc = [0 for i in range(8)] + [fc[0]]
    for i,n in enumerate(new_counters):
        new_fc[n] += fc[i]
    return new_fc

for i in range(80):
    fish_counts = iterate_fish_counts(fish_counts)

print(sum(fish_counts))

for i in range(256-80):
    fish_counts = iterate_fish_counts(fish_counts)

print(sum(fish_counts))

