

with open('aoc-2020/day1-input.txt', 'r') as f:
    input = f.readlines()

input = [int(x) for x in input]
inputLength = len(input)

# part 1
for i in range(0, inputLength):
    for j in range(i + 1, inputLength):
        if input[i] + input[j] == 2020:
            print(input[i], input[j], input[i] * input[j])
            break

# part 2
for i in range(0, inputLength):
    for j in range(i + 1, inputLength):
        if input[i] + input[j] < 2020:
            for k in range(j + 1, inputLength):
                if input[i] + input[j] + input[k] == 2020:
                    print(input[i], input[j], input[k], input[i] * input[j] * input[k])
                    break

def find_prods(input,n):
    sumcombs = [x for x in itertools.combinations(input,n) if sum(x)==2020]
    return prod(sumcombs[0])

