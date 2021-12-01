with open('/aoc-2020/day6-input.txt', 'r') as f:
    resps_list = [x.strip().split('\n') for x in f.read().split('\n\n')]

# Part 1
print(sum(len(set(''.join(resps))) for resps in resps_list))

# Part 2
print(sum(sum(all(q in x for x in resps) for q in set(''.join(resps))) for resps in resps_list))