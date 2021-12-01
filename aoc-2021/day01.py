with open('input/day01-input.txt', 'r') as f:
    input = [int(x) for x in f.readlines()]

def count_increasing_sums(seq,offset):
    print( sum(seq[i+offset]>seq[i] for i in range(len(seq)-offset)) )

print(count_increasing_sums(input,1))
print(count_increasing_sums(input,3))