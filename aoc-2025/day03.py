with open('c:/GitHub/advent-of-code-2020/aoc-2025/input/day03-input.txt', 'r') as f:
    banks = [[int(i) for i in x.strip()] for x in f.readlines()]

def get_max_joltage_ext(bank, size):
    if size==1:
        return max(bank)
    max_val=max(bank[:-size+1])
    max_val_ind=bank.index(max_val)
    return max_val*(10**(size-1)) + get_max_joltage_ext(bank[(max_val_ind+1):],size-1)

print(sum(get_max_joltage_ext(b,2) for b in banks))
print(sum(get_max_joltage_ext(b,12) for b in banks))