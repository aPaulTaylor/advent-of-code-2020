with open('input/day01-input.txt', 'r') as f:
    input = [int(x) for x in f.readlines()]

def count_increases(seq,offset):
    return sum(seq[i+offset]>seq[i] for i in range(len(seq)-offset))

print(count_increases(input,1))
print(count_increases(input,3))