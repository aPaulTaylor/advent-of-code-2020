import itertools

with open('/aoc-2020/day9-input.txt', 'r') as f:
    xmasdata = [int(x) for x in f.readlines()]

# Part 1
for i in range(26, len(xmasdata)):
    prev25 = xmasdata[i - 26:i]
    if not any(sum(x) == xmasdata[i] for x in itertools.combinations(prev25, 2)):
        invalid_num = xmasdata[i]
        break
print(invalid_num)

# Part 2
for i in range(len(xmasdata)):
    cont_sum = xmasdata[i]
    for j in range(i + 1, len(xmasdata)):
        cont_sum += xmasdata[j]
        if cont_sum == invalid_num:
            invalid_sum_range = [xmasdata[n] for n in range(i, j + 1)]
            print(min(invalid_sum_range) + max(invalid_sum_range))
        if cont_sum > invalid_num:
            break

# one-line Part 1
print([xmasdata[i] for i in range(26, len(xmasdata)) if not any(sum(x) == xmasdata[i] for x in itertools.combinations(xmasdata[i - 26:i], 2)) ])

# one-line Part 2
print([min(xmasdata[min(pair):max(pair)+1])+max(xmasdata[min(pair):max(pair)+1]) for pair in itertools.combinations(range(len(xmasdata)),2) if sum(xmasdata[min(pair):max(pair)+1]) == invalid_num])

